import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server pokrenut...")

while True:
    conn, addr = server.accept()

    request = conn.recv(1024).decode()
    print("Primljen zahtev:", request)

    conn.send("Trazeni podaci sa servera".encode())

    conn.close()