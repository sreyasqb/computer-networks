s='192.163.197.1'

def byte_stuffing(data,esc,flag):
    i=0
    while i<len(data):
        if data[i] in [esc,flag]:
            data=data[:i]+esc+data[i:]
            i+=1
        i+=1
    return data
    
def byte_unstuffing(data,esc,flag):
    i,data=0,list(str(int(''.join(data),2)))
    while i<len(data):
        if data[i]==esc:
            data[i]=''
            i+=1
        i+=1
    return ''.join(data)
    

#print(len(bin(13939)[2:]))
#print(len('00010101110000100000000101010001000000000111111100000000000000001011')/17) 
    
#print(byte_unstuffing('00010101110000', '3', '9'))
#print(byte_stuffing(s,'3','9'))

