# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 09:42:00 2021

@author: 20pt33
"""

# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host =socket.gethostname()                   

port = 9994

# connection to hostname on the port.
s.connect((host, port))     
                          

# Receive no more than 1024 bytes
tm = s.recv(1024)           
                       

s.close()

print(tm.decode('ascii'))
