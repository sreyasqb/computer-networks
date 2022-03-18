import socket                                         


# create a socket object
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9994                         

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      
    print("Got a connection from %s" % str(addr))
    #currentTime = time.ctime(time.time()) + "\r\n"
    data=input('type your message : ')
    clientsocket.send(data.encode('ascii'))
    clientsocket.close()
