#file -- use_progressbar.py --
import struct
import sys
import socket
import random
import select
import os
import binascii, zlib
import progressbar

BUFFER_SIZE = 1024

print("NetCopy CLIENT")

if(len(sys.argv) != 4):
    print("Wrong arguments!")
    sys.exit(0)

srv_ip = sys.argv[1]
srv_port = int(sys.argv[2])
file_path = sys.argv[3]


f = open(file_path, "rb")
file_name = f.name

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((srv_ip, srv_port))

l = f.read(1024)
size = os.path.getsize(file_path)
s.send(file_name.encode('utf-8'))
message = s.recv(1024)
print("Server:" + message.decode())
current = 0
print("Start sending.")
while(l):
    progressbar.progressbar(current, size, prefix='Uploading:' + file_name)
    s.send(l)
    l = f.read(BUFFER_SIZE)
    current = current + BUFFER_SIZE
s.close()






