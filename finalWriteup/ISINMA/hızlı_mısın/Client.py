import os
import socket
import requests
import hashlib
import string

def hashString(str):
    shaStr = hashlib.sha256(str.encode()).hexdigest()
    return shaStr


host = socket.gethostname()          # Verilen IP'nin girilmesi gerekli
port = 8888                          # Verilen Portun girilmesi
conn = socket.socket()

conn.connect((host, port))
data = conn.recv(1024)
data = data[26:-1]                  #
print "gelen string : " + data
print hashString(data)
conn.sendall(hashString(data))
data = conn.recv(1024)

conn.close()                         #

print("gelen flag : " + data.decode("utf-8"))
