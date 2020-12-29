# This file is used for sending the file over socket
import os
import socket
import time

# Creating a socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print("Host Name: ", sock.getsockname())

# Accepting the connection.
client, addr = sock.accept()

# Getting file details.
file_name = input("File Name:")
file_size = os.path.getsize(file_name)

# Sending file_name and detail.
client.send(file_name.encode())
client.send(str(file_size).encode())

# Opening file and sending data.
with open(file_name, "rb") as file:
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running loop while c != file_size.
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)

    # Ending the time capture.
    end_time = time.time()

print("File Transfer Complete.Total time: ", end_time - start_time)
# Cloasing the socket.
sock.close()
