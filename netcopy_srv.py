from inspect import Arguments
from os import terminal_size
import struct
import sys
import socket
import random
import select
import binascii, zlib

'''
Arguments:
1: ip
2: port
3: filePath
4: without chekcsum does not work


'''

BUFFER_SIZE = 1024

print("NetCopy SERVER")

if(len(sys.argv) != 4):
    print("Wrong arguments!")
    sys.exit(0)

srv_ip = sys.argv[1]
srv_port = int(sys.argv[2])
file_path = sys.argv[3]

print(srv_ip)
print(srv_port)
print("Downloading path:" + file_path)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((srv_ip, srv_port))
s.listen()

while True:

    client_socket, client_addr = s.accept()
    print("New client connected")
    print(client_addr)

    file_name = client_socket.recv(BUFFER_SIZE)
    client_socket.send("Data recieved".encode())
    file_path = file_path + '\\' + file_name.decode()
    print(file_path)
    f = open(file_path, "wb")

    while True:
        data = client_socket.recv(BUFFER_SIZE)
        if len(data) == 0: 
            print("Client disconnected")
            client_socket.close()
            break

        while(data):
            f.write(data)
            data = client_socket.recv(1024)
        f.close()

    print("File downloaded from client")
s.close()


