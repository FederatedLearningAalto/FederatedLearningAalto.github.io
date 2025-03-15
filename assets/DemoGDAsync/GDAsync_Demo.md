# Introduction to the Asynchronous Gradient Descent Demo

## Overview
This demo showcases an asynchronous gradient descent (GD) algorithm where 
multiple worker nodes communicate and update their local parameters collaboratively. 
The workers interact through a defined topology, exchanging updates to refine 
their optimization process. The key feature of this demo is the use of **Total Variation (TV) Regularization**, 
which enforces smoothness in parameter updates across neighboring workers.

For a theoretical background on decentralized optimization and federated learning, 
refer to **Chapter 5** of the book [Federated Learning](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf).

## Components
The demo consists of the following key components:

### 1. **Main Script [`GDAsync_launch.py`](./GDAsync_launch.py)**
- Defines the worker topology (i.e., how the workers are connected).
- Launches multiple worker processes asynchronously.
- Visualizes the topology using `networkx` and `matplotlib`.

### 2. **Worker Script [`GDAsync_worker.py`](./GDAsync_worker.py)**
- Implements the core logic of each worker.
- Receives updates from its neighbors via TCP sockets.
- Performs gradient descent updates incorporating the TV regularization term.
- Sends updates to its neighbors at regular intervals.

## How It Works
### 1. **Worker Initialization**
Each worker is launched as a separate process and assigned the following parameters:
- `worker_id`: Unique identifier.
- `a_i`: Local offset used in the gradient computation.
- `lr`: Learning rate for updates.
- `alpha`: TV regularization strength.
- `speed`: Controls update frequency.
- `neighbors`: List of other worker IDs it exchanges updates with.

### 2. **Communication and Updates**
- Each worker listens on a unique TCP port (`5000 + worker_id`) to receive updates from its neighbors.
- Periodically, each worker computes an update step, incorporating:
  - **Local gradient**: Derived from `(w - a_i)^2`.
  - **TV gradient**: Encourages smoothness by minimizing differences with neighbors.
- The worker then sends its updated parameter to all neighbors.

### 3. **Topology Visualization**
- A visualization is generated to display worker connections.
- Workers are represented as nodes, with edges indicating communication links.
- Node size is proportional to `speed` (faster workers appear larger).

## Running the Demo
### Step 1: Start the Demo
Run the launcher script:
```bash
python ./GDAsync_launch.py
```
This will start multiple workers and display the topology graph.

### Step 2: Observe Output
Each worker logs:
- Neighbor values received.
- Local and TV gradients.
- Updated parameter value.
- Status messages on communication attempts.

### Step 3: Adjust Worker Configuration
Modify [`GDAsync_launch.py`](./GDAsync_launch.py) to change:
- Number of workers.
- Learning rate (`lr`).
- Regularization strength (`alpha`).
- Worker speed and topology.

## Folder Structure
The expected folder structure is as follows:
```
/demo_folder/
├── GDAsync_launch.py  # Script to launch the workers
├── GDAsync_worker.py  # Script defining worker behavior
```

## Applications
- **Decentralized Optimization**: Suitable for distributed learning scenarios.
- **Federated Learning**: Can be extended to privacy-preserving ML.
- **Consensus Algorithms**: Demonstrates how local updates propagate in a network.

## Future Extensions
- Implement adaptive learning rates.
- Introduce delay and message loss simulation.
- Extend to larger network topologies with real-world data.

## Conclusion
This demo illustrates how asynchronous worker nodes perform optimization 
through collaborative gradient descent with total variation regularization. By 
modifying the topology and parameters, users can explore different decentralized 
learning behaviors. For further insights into the theoretical foundation, refer to 
**Chapter 5** of the book [Federated Learning](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf).

