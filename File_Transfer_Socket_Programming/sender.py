# This file is used to send data to the reciever.
import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print(socket.gethostname())

# Select and open file.
file_name = input("File_name: ")
if os.path.exists(file_name):
    print("File Found")
else:
    print("File Not found")
    exit(0)
file = open(file_name, "rb")
file_data = file.read()
file.close()


client, addr = sock.accept()

# MSG = file_name + "#NEXT$" + file_data
msg = file_name + "#NEXT$" + str(len(file_data))
client.send(msg.encode())

# MSG = file_data
client.sendall(file_data)


client.send("#EXIT$".encode())

client.detach()
sock.close()
