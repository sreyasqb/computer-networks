
import math
import data 
import dijkstra as dj

class IpDatagram:
    def __init__(self,totalLen,headerLen,offset,id):
        self.totalLen=totalLen
        self.headerLen=headerLen
        self.dataLen=totalLen-headerLen
        self.offset=offset
        self.id=id
    def __str__(self):
        return f'pId : {self.id}\ntotalLen : {self.totalLen}\nheaderLen : {self.headerLen}\ndataLen : {self.dataLen}\noffset : {self.offset}\n'

graph=data.graph                         
path=dj.dijkstra(graph,'C','B')
pPath=' -> '.join(path)

print(f'path : {pPath}')
print()


dg=IpDatagram(4800,20,0,'P0')

dataPackets=[dg]

for i in range(len(path)-1):
    fragmentedDataPackets=[]
    mtu=graph[path[i]][path[i+1]]["mtu"]
    # print(mtu)
    pCount=0
    for j,dp in enumerate(dataPackets):
        fCount=(dp.totalLen-dp.headerLen)/(mtu-dp.headerLen)
        fCount=int(math.ceil(fCount))
        for k in range(fCount):
            fdg=IpDatagram(mtu if (mtu-dp.headerLen)*(k+1)<dp.totalLen else dp.totalLen-(mtu-dp.headerLen)*(k),dp.headerLen,mtu*k,f'P{pCount}')
            fragmentedDataPackets.append(fdg)
            pCount+=1
            
    dataPackets=fragmentedDataPackets
    
    print(f'AT ROUTER {path[i+1]}')
    print()
    for i in dataPackets:
        print(i)
        print()

print("AFTER RESSAMBLEING \n")
print(dg)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

