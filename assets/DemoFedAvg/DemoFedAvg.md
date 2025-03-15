# Introduction to the Federated Averaging (FedAvg) Demo

## Overview
This demo illustrates the **Federated Averaging (FedAvg) algorithm**, a key technique in **federated learning**. 
In this setup, multiple clients (workers) train local models on their own data and periodically send updates to 
a central server, which aggregates them to improve a global model.

For a theoretical background on **FedAvg**, refer to **Chapter 5** of the book [Federated Learning](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf).

## Components
This demo consists of three key components:

### 1. **Launcher Script [`FedAvg_launch.py`](./FedAvg_launch.py)**
- Initializes and starts the server process.
- Launches multiple worker processes for local training.
- Handles process termination gracefully.

### 2. **Server Script [`FedAvg_server.py`](./FedAvg_server.py)**
- Manages global model updates.
- Listens for updates from clients and aggregates them.
- Sends updated models back to clients.

### 3. **Worker Script [`FedAvg_worker.py`](./FedAvg_worker.py)**
- Trains a local model using its own data.
- Communicates with the server to exchange model updates.

## Workflow
1. **Start the server**: The server waits for client updates and aggregates their contributions.
2. **Launch worker processes**: Each worker trains locally and periodically sends updates to the server.
3. **Server updates the global model**: The received model updates from workers are averaged and distributed.
4. **Workers continue local training**: The process repeats over multiple rounds to refine the model.
5. **Shutdown handling**: Ensures all processes terminate properly when stopping the demo.

## Running the Demo
### Step 1: Start the Server
Run the server script first:
```bash
python ./FedAvg_server.py
```
This will start the central server and prepare it to receive updates from workers.

### Step 2: Launch Workers
Run the launcher script to start multiple clients (workers):
```bash
python ./FedAvg_launch.py
```
Each worker trains its local model and periodically sends updates to the server.

### Step 3: Observe Output
The logs will display:
- Local training progress on each worker.
- Communication between workers and the server.
- Aggregation process at the server.
- Global model updates over multiple rounds.

### Step 4: Adjust Configuration
Modify [`FedAvg_launch.py`](./FedAvg_launch.py) to adjust parameters such as:
- Number of workers.
- Learning rate (`lr`).
- Aggregation factor (`alpha`).
- Worker speed (simulating computational power).

## Folder Structure
The expected folder structure is as follows:
```
/DemoFedAvg/
├── FedAvg_launch.py  # Script to launch workers and server
├── FedAvg_server.py  # Script managing global model updates
├── FedAvg_worker.py  # Script handling local training and updates
```

## Applications
- **Federated Learning**: Demonstrates a decentralized training approach without sharing raw data.
- **Privacy-Preserving Training**: Workers perform local computations while only sending model updates.
- **Scalable Optimization**: Can be extended to large-scale machine learning tasks.

## Future Extensions
- Implement differential privacy for improved security.
- Add support for heterogeneous data across workers.
- Introduce more advanced aggregation strategies beyond simple averaging.

## Conclusion
This demo provides an implementation of **FedAvg**, highlighting the key aspects of federated learning. By modifying 
parameters and extending the scripts, users can experiment with different training strategies in a decentralized 
learning environment. For further insights, refer to **Chapter 5** of the book [Federated Learning](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf).

