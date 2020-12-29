# This file will be used for recieving files over socket connection.
import os
import socket

host = input("Host Name: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, 22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()
with open("./rec/" + file_name, "wb") as file:
    c = 0
    print("Recieving file")
    while c != file_size:
        data = sock.recv(1024)
        file.write(data)
        c += len(data)
    print("File recieved")
sock.close()
