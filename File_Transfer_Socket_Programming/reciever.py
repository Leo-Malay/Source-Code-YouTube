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

data = sock.recv(100).decode()
file_name, file_size = data.split(",")
file = open("./rec/" + file_name, "wb")
data = sock.recv(int(file_size))
file.write(data)
file.close()

sock.close()
