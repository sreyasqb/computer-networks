class IpDatagram:
    def __init__(self,totalLength,headerLen,offset,id):
        self.totalLength = totalLength
        self.headerLen=headerLen
        self.dataLen=totalLength-headerLen
        self.offset=offset
        self.id=id
    def __str__(self):
        return f'PACKET ID : {self.id}\nTotalLength: {self.totalLength}\nHeaderLen: {self.headerLen}\nDataLen: {self.dataLen}\nOffset: {self.offset}'

graph={
    'A':{
        'R1':{
            "dist":0,
            "mtu":1500,
        }
    },
    'R1':{
        'R2':{
            'dist':3,
            'mtu':620
        },
        'R3':{
            'dist':6,
            'mtu':620
        }
    },
    'R2':{
        'R1':{
            'dist':3,
            'mtu':620
        },
        'R3':{
            'dist':1,
            'mtu':620
        }
    },
    'R3':{
        'R1':{
            'dist':6,
            'mtu':620
        },
        'R2':{
            'dist':1,
            'mtu':620
        },
        'B':{
            'dist':0,
            'mtu':620
        }
    },
    'B':{
        'R3':{
            'dist':0,
            'mtu':620
        }
    }
    
}
def returnShortestPath(graph,source,dest):
    vertices=list(graph.keys())
    source,orSource=source,source
    distance={}
    visited=[]
    
    for v in vertices:
        if v==source :
            distance[v]={"dist":0,"prev":source}
        else :
            distance[v]={"dist":float('inf'),"prev":''}
    i=0
    while len(visited)!=len(vertices)-1:
        nextSource,minDist='',float('inf')
        for v in graph[source]:
            
            if graph[source][v]["dist"]+distance[source]["dist"]<distance[v]["dist"] and v not in visited:
                distance[v]["dist"]=graph[source][v]["dist"]+distance[source]["dist"]
                distance[v]["prev"]=source
                if distance[v]["dist"]<minDist:
                    nextSource=v
                    minDist=distance[v]["dist"]
        visited.append(source)
        source=nextSource
        # print(distance)
    dest=dest
    path=[]
    while dest!=orSource:
        path.append(dest)
        # print(distance[dest]["prev"])
        dest=distance[dest]["prev"]
    path=(path+[orSource])[::-1]
    return path

source,dest='A','B'
path=returnShortestPath(graph,source,dest)
# print(path)

oDg=IpDatagram(5140,20,0,f'P{0}')
dg=IpDatagram(5140,20,0,f'P{0}')
dataPackets=[dg]

print(f'Sending datapackets from {source}\n')

for i in range(len(path)-1):
    fragmentedDataPackets=[]
    mtu=graph[path[i]][path[i+1]]["mtu"]
    off=0
    for dg in dataPackets:
        for i in range((dg.totalLength-dg.headerLen)//(mtu-dg.headerLen)+1):
            if mtu*(i+1)<dg.totalLength:
                fragmentedDataPackets.append(IpDatagram(mtu,dg.headerLen,mtu*i,f'P{i}'))
            else:
                fragmentedDataPackets.append(IpDatagram(dg.totalLength-mtu*i,dg.headerLen,mtu*i,f'P{i}'))
    dg=fragmentedDataPackets

for dg in fragmentedDataPackets:
    print(dg)
    print()
print(f'Recieved packets at {dest}\n')
pathPrint=' -> '.join(path)
print(f'THE SHORTEST PATH IS : [{pathPrint}] for all fragments')
print()
print('Reassembling packets\n')
print(oDg)

    
        
    
