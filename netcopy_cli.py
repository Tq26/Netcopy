import struct
import sys
import socket
import random
import select
import os
import binascii, zlib

print("NetCopy CLIENT")

if(len(sys.argv) != 7):
    print("Wrong arguments!")
    sys.exit(0);

srv_ip = sys.argv[1]
srv_port = int(sys.argv[2])
chsum_srv_ip = sys.argv[3];
chsum_srv_port = int(sys.argv[4]);
file_id = sys.argv[5];
file_path = sys.argv[6];

f = open(file_path, "rb")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((srv_ip, srv_port))

csum = 0
l = f.read(1024)
csum = zlib.crc32(l, csum)

print("Start sending.")
while(l):
    s.send(l)
    l = f.read(1024)
    csum = zlib.crc32(l, csum)
s.close()

print("Sending finished.")

print("Communcation with checksum server started.")
expire_sec = 60
message = "BE|" + file_id + "|" +  str(expire_sec) + "|" + str(len(str(csum))) + "|" + str(csum)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((chsum_srv_ip, chsum_srv_port))
s2.sendall(message.encode('utf-8'))

ans = s2.recv(1024)
print("Checksum server answear:")
print(ans.decode('utf-8'))




