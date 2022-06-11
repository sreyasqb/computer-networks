def printDistance(d):
    for v in d:
        print(f'{v} --> {d[v]["dist"]}')

def dijkstra(graph,source,dest):
    source,orSource=source,source
    dest=dest
    distance={}
    for v in list(graph.keys()):
        if v==source:distance[v]={"dist":0,"prev":''}
        else:distance[v]={"dist":float('inf'),"prev":''}
    visited=[]
    while len(visited)!=len(distance):
        for v in graph[source]:
            if graph[source][v]["dist"]+distance[source]["dist"]<distance[v]["dist"] and v not in visited:
                distance[v]["dist"]=graph[source][v]["dist"]+distance[source]["dist"]
                distance[v]["prev"]=source
        visited.append(source)
        m=float('inf')
        for i in distance:
            if i not in visited and distance[i]["dist"]<m:
                m=distance[i]["dist"]
                source=i
    #printDistance(distance)
    path=[]
    while dest!=orSource:
        path.append(dest)
        dest=distance[dest]["prev"]
    path=(path+[orSource])[::-1]
    return path