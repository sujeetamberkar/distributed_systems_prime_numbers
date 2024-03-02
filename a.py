import socket

def start_client(host, port, numbers):
    """Connect to the server, send numbers, and wait for the modified numbers."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print("Connected to the server.")

            # Send numbers to b.py
            numbers_str = ' '.join(map(str, numbers))
            client_socket.sendall(numbers_str.encode('utf-8'))
            print(f"Sent numbers to b.py: {numbers_str}")

            # Wait for the modified numbers from b.py
            modified_numbers_str = client_socket.recv(1024).decode('utf-8')
            print(f"Received modified numbers from b.py: {modified_numbers_str}")

        except Exception as e:
            print(f"Connection error: {e}")

if __name__ == "__main__":
    HOST = 'localhost'  # Adjust if necessary
    PORT = 16014  # Make sure this matches b.py's listening port
    numbers_input = input("Enter numbers separated by spaces: ")  # Get numbers as a string
    numbers = list(map(int, numbers_input.split()))  # Convert input string to a list of integers
    start_client(HOST, PORT, numbers)
