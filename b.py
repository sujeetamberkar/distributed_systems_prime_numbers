import socket

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def classify_numbers(numbers):
    """Classify numbers into x_input, y_input, z_input."""
    x_input = [n for n in numbers if n in (0, 1)]
    y_input = [n for n in numbers if is_prime(n)]
    z_input = [n for n in numbers if n not in (0, 1) and not is_prime(n)]
    return x_input, y_input, z_input

def forward_list(host, port, numbers):
    """Forward the list of numbers to the specified server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((host, port))
            numbers_str = ' '.join(map(str, numbers))
            sock.sendall(numbers_str.encode('utf-8'))
            print(f"Forwarded {numbers} to port {port}")
        except Exception as e:
            print(f"Connection error with server on port {port}: {e}")

def start_server(host, port):
    """Start the b.py server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                numbers = list(map(int, data.split()))
                
                x_input, y_input, z_input = classify_numbers(numbers)
                
                # Forward the lists to the respective servers
                forward_list(host, 19011, x_input)  # Port for x.py
                forward_list(host, 18012, y_input)  # Port for y.py
                forward_list(host, 17013, z_input)  # Port for z.py
                break  # Break after one iteration for simplicity

if __name__ == "__main__":
    HOST = 'localhost'  # Use the appropriate host
    PORT = 16014  # The port b.py is listening on
    start_server(HOST, PORT)
