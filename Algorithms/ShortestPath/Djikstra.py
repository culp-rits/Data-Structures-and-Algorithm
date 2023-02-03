import sys

def mindist(dist, visited):
    min = INF
    for i in range(n):
        if(min>dist[i] and visited[i] == False):
            min = dist[i]
            index = i
    return index

def djikstra(graph, src):
    dist = [INF]*n
    dist[src] = 0
    visited = [False]*n
    for j in range(n):
        x = mindist(dist, visited)
        visited[x] = True
        for i in range(n):
            if(visited[i] == False and graph[x][i] > 0 and dist[i] > dist[x] + graph[x][i]):
                dist[i] = dist[x] + graph[x][i]
    print(dist)

INF = sys.maxsize
graph = [#insert graph here]
n = 4

djikstra(graph,0)
