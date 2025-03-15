import subprocess
import time
import networkx as nx
import matplotlib.pyplot as plt

# Global TV (Total Variation) regularization factor (same for all workers)
alpha = 10

# Define worker topology and parameters
# Each worker has an ID and attributes: 
# 'a' (some worker-specific parameter), 'neighbors' (list of connected workers),
# 'lr' (learning rate), and 'speed' (processing speed used for visualization)
topology = {
    1: {"a": 1.0, "neighbors": [2], "lr": 0.01, "speed": 10},
    2: {"a": 2.0, "neighbors": [1], "lr": 0.01, "speed": 10}##,
    # Additional workers can be uncommented and added to the topology
    # 3: {"a": 3.0, "neighbors": [1, 2, 4], "lr": 0.1, "speed": 2},
    # 4: {"a": 4.0, "neighbors": [3], "lr": 0.1, "speed": 2}
}

# Launch worker processes
processes = []
for worker_id, data in topology.items():
    # Construct the command for launching a worker subprocess
    cmd = ["python", "GDAsync_worker.py", # Python script to run the worker
           str(worker_id), # Worker ID
           str(data["a"]), # Worker-specific parameter 'a'
           str(data["lr"]), # Learning rate
           str(alpha), # Global regularization factor
           str(data["speed"])]+ list(map(str, data["neighbors"]))   # Append neighbors as command arguments
           
    print(cmd)
    # Start the subprocess for the worker
    p = subprocess.Popen(cmd)
    processes.append(p)
    # Staggered start to avoid overloading resources at the same time
    time.sleep(1) 

# Function to visualize the worker topology

def visualize_topology(topology):
    G = nx.Graph()

    # Add nodes to the graph with a size scaled by the worker's speed
    for worker_id, data in topology.items():
        G.add_node(worker_id, size=data["speed"] * 300)  # Scale node size by speed

    # Add edges to represent connections between workers
    for worker_id, data in topology.items():
        for neighbor in data["neighbors"]: 
            if not G.has_edge(worker_id, neighbor):  # Avoid duplicate edges
                G.add_edge(worker_id, neighbor)

    # Extract node sizes for visualization
    node_sizes = [nx.get_node_attributes(G, 'size')[n] for n in G.nodes()]

    # Draw graph
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, edge_color="gray", font_weight="bold", alpha=0.8)

    plt.title("Worker Topology (Node Size = Speed)")
    plt.show()

# Call visualization function
visualize_topology(topology)

# Wait for all worker processes to finish execution
for p in processes:
    p.wait()
