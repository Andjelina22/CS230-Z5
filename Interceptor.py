import socket

HOST = "127.0.0.1"
PORT = 4000

VALID_TOKEN = "12345"

interceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
interceptor.bind((HOST, PORT))
interceptor.listen(1)

print("Interceptor pokrenut...")

while True:
    client_conn, client_addr = interceptor.accept()

    token = client_conn.recv(1024).decode()

    if token != VALID_TOKEN:
        client_conn.send("Pristup odbijen".encode())
    else:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(("127.0.0.1", 5000))

        server_socket.send("Daj podatke".encode())

        response = server_socket.recv(1024).decode()

        client_conn.send(response.encode())

        server_socket.close()

    client_conn.close()