import socket

def process_numbers(numbers):
    """Process the received numbers by adding 1 to each."""
    return [n * 10 for n in numbers]

def start_server(host, port):
    """Start the server to listen for connections from b.py."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server Y listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")

            with conn:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                numbers = list(map(int, data.split()))
                processed_numbers = process_numbers(numbers)

                # Send the modified numbers back to b.py
                response_str = ' '.join(map(str, processed_numbers))
                conn.sendall(response_str.encode('utf-8'))
                print(f"Processed and sent back: {response_str}")

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 18012  # Ensure this matches the port defined in b.py for y.py
    start_server(HOST, PORT)
