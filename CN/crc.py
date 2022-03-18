def xor(a,b):
    s,a,b=[],a[1:],b[1:]
    for i in range(len(a)):
       if a[i]==b[i]:s.append('0')
       else:s.append('1')
    return s
def bin_div(divident,divisor):
    m,n=len(divident),len(divisor)
    remainder=divident[:n]
    for i in range(m-n+1):
        if remainder[0]=='1':remainder=xor(remainder,divisor)
        else:remainder=xor(remainder,['0']*n)
        if i+n<m:remainder.append(divident[i+n])
    return remainder           

def encode_crc(data,gen):
    data,gen,lgen=list(data),list(gen),len(gen)
    rem=bin_div(data+['0']*(len(gen)-1),gen)
    return data+rem
def decode_crc(data,gen):
    rem=bin_div(list(data),list(gen))
    return 'no error' if ['0']*len(rem)==rem else 'error'
print(*encode_crc('100100','1101'))
print(decode_crc('1001110','1011'))

    
    

