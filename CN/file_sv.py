# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:32:43 2022

@author: 20pt33
"""
import socket
import tqdm
import os

host =socket.gethostname()                   

port = 9994
separator="<SEPARATOR>"
buffer_size=4096

s=socket.socket()
s.bind((host,port))
s.listen(5)
print(f"[*] listening as {host}:{port} ")

client_socket,address=s.accept()
print(f"[+] {address} is connected")

rec=client_socket.recv(buffer_size).decode()
filename,filesize=rec.split(separator)
filename=os.path.join("Z:/", os.path.basename(filename))
filesize=int(filesize)

progress=tqdm.tqdm(range(filesize),f"recieved {filename}",unit="B",unit_scale=True,unit_divisor=1024)
with open(filename,"wb") as f:
    while True:
        bytes_read=client_socket.recv(buffer_size)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))
client_socket.close()
s.close()