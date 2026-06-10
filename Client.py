import socket

HOST = "127.0.0.1"
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

token = input("Unesi token: ")

client.send(token.encode())

response = client.recv(1024).decode()

print("Odgovor:", response)

client.close()