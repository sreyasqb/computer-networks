# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" \

import socket
import tqdm
import os

separator="<SEPARATOR>"
buffer_size=4096

host=socket.gethostname()
port=9994
filename="test_file.py"
filesize=os.path.getsize(filename)

s=socket.socket()
s.connect((host,port))
s.send(f"{filename}{separator}{filesize}".encode())

progress=tqdm.tqdm(range(filesize),f"Sending {filename}",unit="B",unit_scale=True,unit_divisor=1024)
with open(filename,"rb") as f:
    while 1:
        bytes_read=f.read(buffer_size)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.close()