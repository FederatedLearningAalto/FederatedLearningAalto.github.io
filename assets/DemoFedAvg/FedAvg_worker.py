"""
This script implements a **worker (client) for Synchronous Gradient Descent (SGD)**
in a federated learning setup. Each worker:

1. **Communicates with the central server** to send model updates.
2. **Listens for synchronization signals** from the server.
3. **Receives updated model parameters** from other workers via the server.
4. **Updates its local model parameters** using gradient descent.
5. **Interacts with neighboring workers** (if applicable) to regularize updates.
6. **Simulates processing delays** based on an adjustable speed factor.

### **Workflow**
1. Worker initializes with:
   - A unique worker ID.
   - A local parameter `a` used in training.
   - Learning rate and update smoothing parameters.
   - A speed factor to simulate computational variability.
2. Worker sends its current state (`w`) to the server.
3. Worker **waits for synchronization** before continuing.
4. Upon sync, it receives **updated neighbor parameters** from the server.
5. Updates `w` using:
   - Local gradient descent.
   - A smoothing term from neighboring worker values.
6. The process repeats until manually stopped.

### **Files Involved**
- `server.py`: Coordinates synchronization and model aggregation.
- `worker.py` (this script): Simulates a client participating in gradient updates.
- `launcher.py`: Orchestrates execution of all components.

Press **Ctrl+C** to stop execution and gracefully shut down the worker.

Author: [Your Name]
Date: [YYYY-MM-DD]
"""

import socket
import threading
import pickle
import time
import sys
import signal

class Worker:
    def __init__(self, worker_id, local_a, neighbors, lr, alpha, speed, server_port=5000):
        """
        Initialize a worker node in the Synchronous GD setup.
        
        Args:
            worker_id (int): Unique identifier for the worker.
            local_a (float): Local parameter influencing updates.
            neighbors (list): List of neighboring worker IDs.
            lr (float): Learning rate for gradient descent.
            alpha (float): Regularization factor for TV gradient.
            speed (int): Controls simulated processing speed.
            server_port (int): Port number where the central server runs.
        """
        self.worker_id = worker_id
        self.local_a = local_a
        self.neighbors = set(neighbors)  # Neighboring worker IDs
        self.lr = lr
        self.alpha = alpha
        self.speed = speed
        self.w = 0.0  # Worker parameter (model weight)
        self.recv_w = 0.0  # Latest received global model params 
        self.received_updates = set()  # Track updates from neighbors
        self.lock = threading.Lock()  # Ensure safe access to shared data
        self.running = True  # Control worker shutdown

        self.listen_port = 5000 + worker_id  # Worker listens on ports starting from 5001
        self.server_port = server_port  # Central server is at port 5000

    def send_update_to_server(self):
        """Send the current weight `w` to the central server."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", self.server_port))
                s.sendall(pickle.dumps((self.worker_id, self.w)))
                print(f"Worker {self.worker_id}: Sent update w = {self.w:.4f} to server")
        except Exception as e:
            print(f"Worker {self.worker_id}: Failed to send update to server - {e}")

    def receive_updates_from_server(self):
        """Receive updated worker values from the server after synchronization."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(("127.0.0.1", self.listen_port))
                s.listen()
                conn, _ = s.accept()
                with conn:
                    data = conn.recv(4096)
                    if data:
                        updated_values = pickle.loads(data)
                        print(f"Worker {self.worker_id}: Received updated values from server: {updated_values}")
                        self.recv_w = updated_values
        except Exception as e:
            print(f"Worker {self.worker_id}: Error receiving updates from server - {e}")
        finally:
            time.sleep(0.1)  # Short delay before retrying if necessary

    def run(self):
        """
        Main worker loop:
        1. Sends initial update to the server.
        2. Waits for synchronization before updating parameters.
        3. Receives updates from the server.
        4. Computes gradient updates and adjusts `w`.
        5. Loops until termination.
        """
        while self.running:
            self.send_update_to_server()
            self.receive_updates_from_server()  # Receive updated parameters from neighbors

           

            # Compute TV (total variation) gradient based on neighbors
            with self.lock:
                # Compute local gradient
                gradient = 2 * (self.recv_w - self.local_a)
                

            # Perform gradient descent update
            self.w -= self.lr * gradient
            print(f"Worker {self.worker_id}: Updated w = {self.w:.4f}")

            time.sleep(3.0 / self.speed)  # Simulate computation time based on speed factor

    def stop(self):
        """Gracefully stop the worker and release the network port."""
        self.running = False
        print(f"Worker {self.worker_id}: Stopping and releasing port {self.listen_port}.")
        sys.exit(0)

if __name__ == "__main__":
    worker_id = int(sys.argv[1])
    local_a = float(sys.argv[2])
    lr = float(sys.argv[3])
    alpha = float(sys.argv[4])
    speed = float(sys.argv[5])
    neighbors = list(map(int, sys.argv[6:]))  # Neighboring worker IDs

    worker_instance = Worker(worker_id, local_a, neighbors, lr, alpha, speed)

    # Handle termination properly (Ctrl+C)
    signal.signal(signal.SIGINT, lambda sig, frame: worker_instance.stop())

    worker_instance.run()
