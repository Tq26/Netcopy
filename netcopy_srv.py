from os import terminal_size
import struct
import sys
import socket
import random
import select
import binascii, zlib


print("NetCopy SERVER")

if(len(sys.argv) != 7):
    print("Wrong arguments!")
    sys.exit(0);

srv_ip = sys.argv[1]
srv_port = int(sys.argv[2])
chsum_srv_ip = sys.argv[3];
chsum_srv_port = int(sys.argv[4]);
file_id = sys.argv[5];
file_path = sys.argv[6];

print(srv_ip)
print(srv_port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((srv_ip, srv_port))
s.listen()

client_socket, client_addr = s.accept()
print("New client connected")
print(client_addr)
f = open(file_path, "wb")
while True:
    data = client_socket.recv(1024)
    if len(data) == 0: 
        print("Client disconnected")
        client_socket.close()
        break
        
    while(data):
        f.write(data)
        data = client_socket.recv(1024)
    f.close()

s.close()

print("File downloaded from client")

f2 = open(file_path, "rb")
l = True
csum = 0

while(l):
    l = f2.read(1024)
    csum = zlib.crc32(l,csum)

message = str("KI|" + file_id)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((chsum_srv_ip, chsum_srv_port))
print("Communcation with checksum server started.")
s2.sendall(message.encode('utf-8'))

data = s2.recv(1024)
data = data.decode('utf-8')
if data == "0|":
    print("CSUM CORRUPTED")
else:
    pass
    csum2 = data.split('|')[1]
    
    if str(csum2) == str(csum):
        print("CSUM OK")
    else:
        print("CSUM CORRUPTED")

