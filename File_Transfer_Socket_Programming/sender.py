# This file is used for sending the fileover socket
import os
import socket

file_name = input("File_name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)

client, addr = sock.accept()

client.send(file_name.encode())
client.send(os.path.getsize(file_name).encode())
with open(file_name, "wb") as file:
    c = 0
    print("Sending file")
    while c <= os.path.getsize(file_name):
        data = file.read(1024)
        client.send(data)
        c += len(data)
    print("File sent")

sock.close()
