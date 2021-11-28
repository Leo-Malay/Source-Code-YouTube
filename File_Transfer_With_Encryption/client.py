# This file will be used for recieving files over socket connection.
import os
import socket
import time
from security import decrypt

host = input("Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying to connect to socket.
try:
    sock.connect((host, 22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

# Send file details.
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

# Opening and reading file.
with open("./rec/" + file_name, "wb") as file:
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running the loop while file is recieved.
    while c <= int(file_size):
        data = sock.recv(1464)
        if not (data):
            break
        dec_data = decrypt(data)
        file.write(dec_data)
        c += len(dec_data)

    # Ending the time capture.
    end_time = time.time()

print("File transfer Complete.Total time: ", end_time - start_time)

# Closing the socket.
sock.close()
