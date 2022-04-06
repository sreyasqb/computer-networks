import socket as s
import crc as c
import byte_stuffing as b

gen='1011'
esc='3'
flag='9'
macAddress='00:0C:42:A9:95:8B'
client=s.socket()
host=s.gethostname()
port=3000
client.connect((host,port))
client.send(macAddress.encode())
decodedFrames=[]
while True:
    # max number in byte_stuffing in ip is 199.x.x.x
    tm=client.recv(17) # 14 bits from byte_stuffing and 3 from crc
    if len(tm)==0:break
    frame=tm.decode('ascii')
    decodedFrames.append(c.decode_crc(frame, gen))

unstuffedFrames='.'.join(list(map(lambda x:b.byte_unstuffing(x, esc, flag),decodedFrames)))
print(unstuffedFrames)
client.close()
    
    