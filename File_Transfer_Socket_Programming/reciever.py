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

data = ""
while data != "#EXIT$":
    data = sock.recv(1024).decode()
    if data == "#EXIT$":
        break
    data = data.split("#NEXT$")
    file_name, file_size = data[0], int(data[1])
    file = open("./rec/" + file_name, "wb")
    data = sock.recv(file_size)
    file.write(data)
    file.close()

sock.close()
