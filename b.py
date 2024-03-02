import socket
import threading
from queue import Queue

# Define ports for backend servers
PORT_X = 19011
PORT_Y = 18012
PORT_Z = 17013

# Queue to hold responses from backend servers
responses = Queue()

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def classify_numbers(numbers):
    """Classify numbers into x_input, y_input, z_input based on their values."""
    x_input = [n for n in numbers if n in (0, 1)]
    y_input = [n for n in numbers if is_prime(n)]
    z_input = [n for n in numbers if n not in (0, 1) and not is_prime(n)]
    return x_input, y_input, z_input

def send_numbers_to_backend(numbers, port):
    """Send numbers to a specified backend server and collect the response."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', port))
        numbers_str = ' '.join(map(str, numbers))
        sock.sendall(numbers_str.encode('utf-8'))
        response = sock.recv(1024).decode('utf-8')
        response_numbers = list(map(int, response.split()))
        for number in response_numbers:
            responses.put(number)

def handle_client_connection(client_conn):
    """Handle incoming connection from a.py, classify numbers, send them to backends, and return the aggregated response."""
    with client_conn:
        data = client_conn.recv(1024).decode('utf-8')
        numbers = list(map(int, data.split()))
        x_input, y_input, z_input = classify_numbers(numbers)

        # Create threads to send numbers to backend servers and wait for responses
        threads = []
        if x_input:
            threads.append(threading.Thread(target=send_numbers_to_backend, args=(x_input, PORT_X)))
        if y_input:
            threads.append(threading.Thread(target=send_numbers_to_backend, args=(y_input, PORT_Y)))
        if z_input:
            threads.append(threading.Thread(target=send_numbers_to_backend, args=(z_input, PORT_Z)))

        # Start threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Collect and send aggregated responses back to a.py
        aggregated_response = [responses.get() for _ in range(responses.qsize())]
        response_str = ' '.join(map(str, aggregated_response))
        client_conn.sendall(response_str.encode('utf-8'))

def start_server(host, port):
    """Start the b.py server to listen for connections from a.py."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            client_conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            handle_client_connection(client_conn)

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 16014
    start_server(HOST, PORT)
