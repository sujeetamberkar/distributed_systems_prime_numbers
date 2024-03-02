import socket

def start_client(host, port, numbers):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print("Connected to the server.")
            client_socket.sendall(numbers.encode('utf-8'))
        except Exception as e:
            print(f"Connection error: {e}")

if __name__ == "__main__":
    HOST = 'localhost'  # Adjust if necessary
    PORT = 16014  # Make sure this matches b.py's listening port
    numbers = input("Enter numbers separated by spaces: ")  # Get numbers as a string
    start_client(HOST, PORT, numbers)
