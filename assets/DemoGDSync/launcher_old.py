"""
This script implements a **launcher for a Synchronous Gradient Descent (SGD) demo**
using `client.py` and `server.py`. The demo simulates a federated learning setup
where multiple clients (workers) collaborate with a central server to perform
synchronous gradient descent updates.

### **Workflow**
1. **Generate a worker topology**: Workers are connected in a network structure.
2. **Visualize the topology**: The network graph is displayed for better understanding.
3. **Start the server**: The central server listens for updates from clients.
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
import random
import networkx as nx
import matplotlib.pyplot as plt
import signal
import sys

# Global variables to track processes
server_process = None
worker_processes = []

def generate_topology(num_workers, connectivity=2):
    """
    Generate a random network topology where each worker is connected to
    a limited number of neighbors, forming a structured communication graph.
    
    Args:
        num_workers (int): Total number of workers in the system.
        connectivity (int): Number of neighbors each worker connects to.
    
    Returns:
        tuple: A dictionary representing the topology and a NetworkX graph object.
    """
    G = nx.barabasi_albert_graph(num_workers, connectivity)

    topology = {i: [] for i in range(1, num_workers + 1)}
    for edge in G.edges():
        w1, w2 = edge
        topology[w1 + 1].append(w2 + 1)
        topology[w2 + 1].append(w1 + 1)

    return topology, G

def visualize_topology(G, topology):
    """
    Visualize the worker network topology using NetworkX.
    
    Args:
        G (networkx.Graph): The generated worker connectivity graph.
        topology (dict): Dictionary representation of worker connections.
    """
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1000, font_size=12)
    plt.title("Worker Network Topology")
    plt.show()

def start_server(worker_ids):
    """
    Start the SGD synchronization server on port 5000.
    
    Args:
        worker_ids (list): List of worker IDs to be managed by the server.
    """
    global server_process
    server_process = subprocess.Popen(
        ["python", "server.py"] + list(map(str, worker_ids)))
    time.sleep(5)  # Ensure the server is fully started before workers are launched


def start_workers(topology, learning_rate=0.1, alpha=0.5, speed=2):
    """
    Start worker processes based on the generated network topology.
    
    Args:
        topology (dict): The worker connectivity topology.
        learning_rate (float): Learning rate used in training.
        alpha (float): Weighting factor for updates.
        speed (int): Processing speed simulation.
    """
    global worker_processes
    for worker_id, neighbors in topology.items():
        cmd = [
            "python", "worker.py",
            str(worker_id), str(worker_id),  # Local a_i is set as worker_id
            str(learning_rate), str(alpha), str(speed)
        ] + list(map(str, neighbors))

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
    connectivity = 2  # Number of neighbors per worker
    
    # Generate and visualize the worker topology
    topology, G = generate_topology(num_workers, connectivity)

    print("\nVisualizing topology...")
    visualize_topology(G, topology)

    print("\nStarting server on port 5000...")
    start_server(list(topology.keys()))

    print("\nStarting workers on ports 5001, 5002, ...")
    start_workers(topology)

    # Handle termination properly
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown())

    # Keep the launcher running
    while True:
        time.sleep(1)
