import socket
import threading

CLIENT_PORT = 4000
SERVER_PORT = 5000

def process_request(filename, callback_port):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("127.0.0.1", SERVER_PORT))

    server_socket.send(filename.encode())

    result = server_socket.recv(1024).decode()

    server_socket.close()

    callback_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    callback_socket.connect(("127.0.0.1", callback_port))

    callback_socket.send(result.encode())

    callback_socket.close()

middleware = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
middleware.bind(("127.0.0.1", CLIENT_PORT))
middleware.listen()

print("Middleware pokrenut...")

while True:
    conn, addr = middleware.accept()

    data = conn.recv(1024).decode()

    filename, callback_port = data.split(";")

    conn.send("Zahtev primljen".encode())

    threading.Thread(
        target=process_request,
        args=(filename, int(callback_port))
    ).start()

    conn.close()