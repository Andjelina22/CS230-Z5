import socket
import threading

CALLBACK_PORT = 6000

def callback_listener():

    callback_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    callback_server.bind(("127.0.0.1", CALLBACK_PORT))
    callback_server.listen(1)

    conn, addr = callback_server.accept()

    result = conn.recv(1024).decode()

    print("\nCALLBACK:", result)

    conn.close()
    callback_server.close()

threading.Thread(target=callback_listener).start()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 4000))

filename = input("Unesi naziv fajla: ")

client.send(f"{filename};{CALLBACK_PORT}".encode())

response = client.recv(1024).decode()

print(response)

client.close()