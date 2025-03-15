"""
This script implements a **launcher for a FedAvg demo**
using `FedAvg_worker.py` and `FedAvg_server.py`. The demo simulates a federated learning setup
where multiple clients (workers) collaborate with a central server to train a global 
model 

### **Workflow**
1. **Generate a worker topology**: Workers are connected in a network structure.
2. **Visualize the topology**: The network graph is displayed for better understanding.
3. **Start the server**: The central server listens for updates from clients and distributes only neighbor updates.
4. **Launch worker processes**: Each worker trains locally and communicates with the server.
5. **Shutdown handling**: Ensures all processes are terminated gracefully upon exit.

### **Files Involved**
- `launcher.py`: Orchestrates the execution of the demo.
- `server.py`: Manages global model updates and client coordination.
- `worker.py`: Simulates local training and model updates.

Press **Ctrl+C** to stop the execution and shut down all processes.

Author: Alexander Jung
Date: 2025-03-15
"""

import subprocess
import time
import networkx as nx
import matplotlib.pyplot as plt
import signal
import sys

# Global variables to track processes
server_process = None
worker_processes = []



def start_server(worker_ids):
    """
    Start the SGD synchronization server on port 5000, passing the worker topology.
    
    Args:
        worker_ids (list): List of worker IDs to be managed by the server.
        topology (dict): Dictionary containing worker connectivity.
    """
    global server_process
    server_process = subprocess.Popen(
        ["python", "FedAvg_server.py"] + list(map(str, worker_ids)) )
    time.sleep(5)  # Ensure the server is fully started before workers are launched

def start_workers(num_clients,learning_rate=0.1, alpha=0.5, speed=2):
    """
    Start worker processes based on the generated network topology.
    
    Args:
        topology (dict): The worker connectivity topology.
        learning_rate (float): Learning rate used in training.
        alpha (float): Weighting factor for updates.
        speed (int): Processing speed simulation.
    """
    global worker_processes
    for worker_id in range(1,num_clients+1):
        cmd = [
            "python", "FedAvg_worker.py",
            str(worker_id), str(worker_id),  # Local a_i is set as worker_id
            str(learning_rate), str(alpha), str(speed)
        ] 
        
        proc = subprocess.Popen(cmd)
        worker_processes.append(proc)

def shutdown():
    """
    Gracefully terminate all processes when Ctrl+C is pressed.
    Ensures all worker and server processes are stopped properly.
    """
    print("\nShutting down all processes...")
    
    # Terminate workers
    for proc in worker_processes:
        proc.terminate()
    
    # Terminate server
    if server_process:
        server_process.terminate()
    
    print("All processes terminated successfully.")
    sys.exit(0)

if __name__ == "__main__":
    num_workers = 5  # Number of workers


    print("\nStarting server on port 5000...")
    start_server(list(range(1,num_workers+1)))

    print("\nStarting workers on ports 5001, 5002, ...")
    start_workers(num_workers)

    # Handle termination properly
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown())

    # Keep the launcher running
    while True:
        time.sleep(1)
