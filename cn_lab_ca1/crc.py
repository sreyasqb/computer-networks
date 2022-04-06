def xor(a,b):
    ans=[]

    for i in range(len(a)):
        if a[i]==b[i]:
            ans.append('0')
        else:
            ans.append('1')
    
    return ans

def binDiv(dividend,divisor):
    rem,m,n=dividend[:len(divisor)],len(dividend),len(divisor)
    for i in range(m-n+1):
        
        if rem[0]=='1':
            rem=xor(rem,divisor)
        else:
            rem=xor(rem,['0']*n)
        if i!=m-n:
            rem=rem[1:]+[dividend[i+n]]
    return rem[1:]
    

def crc(data,gen):
    data,gen=list(data),list(gen)
    newData=data+(len(gen)-1)*['0']
    ans=data+binDiv(newData,gen)
    return ''.join(ans)

def decode_crc(data,gen):
    data,gen=list(data),list(gen)
    if binDiv(data,gen)==(len(gen)-1)*['0']:
        return ''.join(data[:len(data)-3])
    else:
        return 0
#print(decode_crc('1001110','1011'))

    
#print(crc('1001','1011'))
