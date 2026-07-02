import socket


HOST = "127.0.0.1"

PORT = 5004


server = socket.socket()
server.bind((HOST,PORT))
server.listen()

print("server started...")

print("waiting for clients...")


client, address =  server.accept()

print("connected:",address)


message = client.recv(1024).decode()

print("message:",message)

client.close()
server.close()