import socket

client = socket.socket()
client.connect(("127.0.0.1",5004))

client.send("hello server!".encode())

print(client.recv(1024).decode())

client.close()