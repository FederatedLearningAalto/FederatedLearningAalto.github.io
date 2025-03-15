"""
This script implements a **server for Synchronous Gradient Descent (SGD)**
in a Federated Learning setup. The server:

1. Listens for connections from multiple client workers.
2. Receives locally trained model updates from clients.
3. Aggregates updates using FedAvg (Federated Averaging).
4. Sends each worker **only the updated parameters of its neighbors**.
5. Uses multi-threading to handle multiple clients simultaneously.

The server remains active until manually terminated (Ctrl+C).

Author: Alex Jung
Date: 2025-Mar-15
"""

import socket
import threading
import pickle
import sys
import signal
import time

class SGDServer:
    def __init__(self, worker_ids, worker_topology, port=5000):
        """
        Initialize the server for Synchronous GD.
        
        Args:
            worker_ids (list): List of expected worker IDs.
            worker_topology (dict): Dictionary mapping workers to their neighbors.
            port (int): Port number for the server.
        """
        self.worker_ids = set(worker_ids)  # Expected worker IDs
        self.worker_topology = worker_topology  # Worker connectivity
        self.worker_updates = {}  # Store received updates from workers
        self.lock = threading.Lock()  # Thread safety for shared data
        self.port = port  # Server port
        self.round = 0  # Synchronization round counter
        self.server_socket = None  # Placeholder for server socket
        self.running = True  # Control server shutdown

    def handle_worker(self, conn, addr):
        """Handles worker updates and synchronizes training steps."""
        try:
            while self.running:
                data = conn.recv(1024)
                if not data:
                    break
                
                worker_id, w_value = pickle.loads(data)  # Receive worker ID and local parameter

                with self.lock:
                    self.worker_updates[worker_id] = w_value
                    print(f"Server: Received w={w_value:.4f} from Worker {worker_id}")

                    # Wait for all workers before sending updates
                    if len(self.worker_updates) == len(self.worker_ids):
                        self.round += 1
                        print(f"\n--- Server: Synchronization Round {self.round} ---")
                        print("Server: All workers sent their updates, broadcasting to neighbors...\n")

                        # Create per-worker updates containing only their neighbors' data
                        updates_per_worker = {
                            worker_id: {
                                neighbor_id: self.worker_updates[neighbor_id]
                                for neighbor_id in self.worker_topology.get(worker_id, [])
                                if neighbor_id in self.worker_updates
                            }
                            for worker_id in self.worker_ids
                        }

                        # Reset updates for the next iteration
                        self.worker_updates.clear()

                        # Send updates only to relevant workers
                        for worker_id, updates in updates_per_worker.items():
                            self.send_updated_parameters(worker_id, updates)
        
        except Exception as e:
            print(f"Server: Error handling worker {worker_id}: {e}")

    def send_updated_parameters(self, worker_id, updates, max_retries=5, delay=1):
        """Send the updated parameters of only the neighbors to each worker."""
        worker_port = 5000 + worker_id  # Worker ports start from 5001

        for attempt in range(max_retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(("127.0.0.1", worker_port))
                    s.sendall(pickle.dumps(updates))  # Send only neighbors' updated values
                print(f"Server: Sent neighbor updates to Worker {worker_id} on port {worker_port}")
                return  # Success, exit function
            except Exception as e:
                print(f"Server: Failed to send updates to Worker {worker_id} on port {worker_port}, Retrying ({attempt+1}/{max_retries})...")
                time.sleep(delay)  # Wait before retrying

    def start(self):
        """
        Start the server and listen for worker updates.
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow socket reuse after shutdown

        try:
            self.server_socket.bind(("127.0.0.1", self.port))  # Bind server to localhost and specified port
            self.server_socket.listen()  # Start listening for incoming connections
            print(f"Server: Listening on port {self.port}... (Press Ctrl+C to stop)")

            while self.running:
                # Wait for a client to connect (blocking call)
                conn, addr = self.server_socket.accept()
                print(f"Server: Accepted connection from {addr}")
                
                # Spawn a new thread to handle the client
                threading.Thread(target=self.handle_worker, args=(conn, addr), daemon=True).start()
        
        except KeyboardInterrupt:
            # If the user presses Ctrl+C, shut down gracefully
            self.shutdown()
        finally:
            # Ensure the socket is closed when exiting
            self.server_socket.close()

    def shutdown(self):
        """
        Gracefully shutdown the server.
        """
        print("\nServer shutting down...")
        self.running = False  # Stop the server loop
        self.server_socket.close()  # Close the socket to free up the port
        print("Server: Port released successfully.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python server.py <worker_id_1> <worker_id_2> ... --topology <worker_id:neighbor1,neighbor2,...>")
        sys.exit(1)
    
    args = sys.argv[1:]
    split_index = args.index("--topology")
    worker_ids = list(map(int, args[:split_index]))
    topology_args = args[split_index + 1:]
    
    worker_topology = {}
    for entry in topology_args:
        worker_id, neighbors = entry.split(":")
        worker_topology[int(worker_id)] = list(map(int, neighbors.split(",")))
    
    print(f"Server initialized with workers: {worker_ids}")
    print(f"Worker topology: {worker_topology}")

    server = SGDServer(worker_ids, worker_topology)

    # Handle termination properly
    signal.signal(signal.SIGINT, lambda sig, frame: server.shutdown())

    server.start()