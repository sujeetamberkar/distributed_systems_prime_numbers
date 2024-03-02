import socket

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Listening on {host}:{port}")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Here, implement the logic specific to y.py's purpose
                print(f"Received {data.decode('utf-8')}")

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 18012  # Ensure this matches the port forwarded to by b.py
    start_server(HOST, PORT)
