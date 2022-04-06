import socket as s
import crc as c
import byte_stuffing as b
gen='1011'
esc='3'
flag='9'
ipMac={'00:0C:42:A9:95:8B':'192.168.127.1','10:93:E9:09:09:50:04':'192.168.172.3',
      '18:B4:30:05:CA:3C':'192.168.127.3','28:CF:DA:05:5F:99':'192:168:127:13',
      '3C:07:54:09:EC:CD':'192.168.2.1'}
server=s.socket()

host=s.gethostname()
port=3000
server.bind((host,port))
server.listen()

def parseIp(ip):
    ip=list(map(lambda x:bin(int(x))[2:].zfill(14),ip.split('.')))
    return ip

while True:
    client,addr=server.accept()
    data=client.recv(1024).decode()
    #print(ipMac[data])
    binIp=parseIp(b.byte_stuffing(ipMac[data], esc, flag))
    #print(binIp)
    encodedIp=list(map(lambda x:c.crc(x,gen),binIp))
    #print(encodedIp)
    msg=''.join(encodedIp)
    print(f" this is the msg :\n{msg}")
    client.send(msg.encode('ascii'))
    
    client.close()