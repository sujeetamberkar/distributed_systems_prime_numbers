# Distributed System Middle Layer

This project demonstrates a simple yet functional distributed system using Python and socket programming. It is designed to showcase how a client interface can interact with backend servers through a middle layer, facilitating a basic understanding of distributed systems architecture.

## Architecture

The project is structured into four main components:

- **Client Interface (`a.py`)**: The user-facing component that sends a series of numbers to the middle layer for processing.
- **Middle Layer (`b.py`)**: Acts as an intermediary between the client interface and the backend servers. It classifies the numbers received from the client interface and forwards them to the appropriate backend server based on specific criteria.
- **Backend Servers (`x.py`, `y.py`, `z.py`)**: These servers process the numbers sent by the middle layer. Each server has a unique role or processing logic, and after processing, they send the numbers back to the middle layer.
- **The middle layer (`b.py`)** then aggregates the processed numbers from all backend servers and sends them back to the client interface.

## How to Run

Follow these steps to run the distributed system on your local machine:

### Step 1: Start All Backend Servers

Open a terminal window for each backend server and start them using the following commands:

```sh
python x.py
python y.py
python z.py
```

Make sure each server is running before proceeding to the next step.

### Step 2: Start the Middle Layer

In a new terminal window, start the middle layer:

```sh
python b.py
```

Wait for confirmation that the middle layer is listening for connections before moving to the next step.

### Step 3: Start the Client Interface

Finally, in another terminal window, start the client interface:

```sh
python a.py
```

Follow the on-screen prompts to enter the numbers you wish to process.

## Project Structure

- `a.py`: The client interface that sends numbers to be processed.
- `b.py`: The middle layer that routes numbers to the appropriate backend server and aggregates the results.
- `x.py`, `y.py`, `z.py`: Backend servers that process numbers in different ways.

## Dependencies

- Python 3.x
- No external libraries are required.

