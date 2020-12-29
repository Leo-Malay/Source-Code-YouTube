# This file is used to send data to the reciever.
import os
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print("Host Name: ", sock.getsockname())

# Select and open file.
file_name = input("Enter File Name: ")
if os.path.exists(file_name):
    print("File Found")
else:
    print("File Not found")
    exit(0)
file = open(file_name, "rb")
file_data = file.read()
file.close()

print("File is ready to be sent")
client, addr = sock.accept()

query = file_name + "," + str(len(file_data))
client.send(query.encode())
client.send(file_data)

print("File sent")
sock.close()
