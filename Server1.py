import socket
import time

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server pokrenut...")

while True:
    conn, addr = server.accept()

    request = conn.recv(1024).decode()

    print("Pretraga za:", request)

    time.sleep(5)  # simulacija duze obrade

    result = f"Fajl '{request}' je pronadjen"

    conn.send(result.encode())

    conn.close()