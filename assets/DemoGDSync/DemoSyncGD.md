# Synchronous Gradient Descent (SGD) Demo

## Overview
This demo implements **Synchronous Gradient Descent (SGD)** in a federated learning setup, where 
multiple workers (clients) collaborate with a central server to train a model. The server synchronizes 
updates across workers and ensures that each worker only receives updates from its **designated neighbors** 
based on a predefined network topology.

For a theoretical background on **Synchronous Gradient Descent in Federated Learning**, refer to 
**Chapter 5** of [this book](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf).

## Key Features
- **Federated Learning Setup**: Workers train locally and communicate updates with the server.
- **Synchronous Gradient Descent**: The server waits for all worker updates before proceeding to the next iteration.
- **Neighbor-Based Communication**: Workers receive updated parameters only from their designated neighbors.
- **Multi-threaded Server**: Handles multiple clients simultaneously for efficient processing.
- **Graph-Based Topology**: Workers are structured in a connected network for distributed updates.

## Files Included
- `launcher.py`
  - Initializes the system and generates a **random worker topology** using NetworkX.
  - Starts the **server** and **worker clients**.
  - Manages graceful termination of all processes.
- `server.py`
  - Listens for worker updates and aggregates them.
  - Synchronizes training rounds and sends **neighbor-specific updates** back to each worker.
- `worker.py`
  - Trains a local model using gradient descent.
  - Communicates with the **server** to send updates and receive neighbor updates.
  - Incorporates neighbor information in its gradient descent step.

## How It Works
### 1. Topology Generation
- `launcher.py` generates a **random connected graph**, defining worker-to-worker connections.
- The topology is displayed using NetworkX visualization.

### 2. Server and Worker Initialization
- The **server** starts first, listening for incoming worker connections.
- Each **worker** initializes with:
  - A local model parameter `w`.
  - Learning rate (`lr`), regularization (`alpha`), and computation speed (`speed`).
  - Neighbor information to incorporate in training.

### 3. Training & Synchronization
- Each worker trains **locally** and sends `w` to the server.
- The **server waits** until all workers submit updates.
- Once all updates are collected, the server distributes **only neighbor-specific updates** back to each worker.
- Workers update their `w` using their own gradient **and their neighbors' information**.

### 4. Iteration Continues
- The process repeats for multiple rounds until stopped manually.

## Running the Demo
### Prerequisites
Ensure you have **Python 3** installed and required dependencies:
```bash
pip install networkx matplotlib
```

### Running the Simulation
The script does not take command-line arguments directly. To configure the number of workers and connectivity, modify `launcher.py` as needed.

Press **Ctrl+C** to stop execution and shut down all processes.

## Expected Output
### Topology Visualization
- Displays the network structure of workers.

### Server Logs
```bash
Server: Listening on port 5000... (Press Ctrl+C to stop)
Server: Received w=0.4321 from Worker 1
Server: Received w=0.3210 from Worker 2
Server: Received w=0.6789 from Worker 3
...
Server: Sent neighbor updates to Worker 1 on port 5001
Server: Sent neighbor updates to Worker 2 on port 5002
...
```

### Worker Logs
```bash
Worker 1: Received neighbor updates: {2: 0.3210, 3: 0.6789}
Worker 2: Updated w = 0.4567
...
```

## Customization
- Modify `launcher.py` to set the **number of workers** and **network topology**.
- Adjust **learning rate** (`lr`) and **regularization** (`alpha`) in `worker.py`.
- Experiment with different aggregation strategies in `server.py`.

## Next Steps
- Implement **asynchronous gradient descent** where workers do not have to wait for all others.
- Experiment with **different topologies** to see how network structure affects convergence.
- Extend the system to use **real datasets and models** instead of toy parameters.

## Author
Alexander Jung, 2025-03-15