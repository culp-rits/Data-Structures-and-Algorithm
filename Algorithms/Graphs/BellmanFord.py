import sys

def bellmanford(graph,n,src):
    dist = [INF]*n
    dist[src] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(graph[i][j] != INF and dist[i] != INF and dist[i] + graph[i][j] < dist[j]):
                    dist[j] = dist[i] + graph[i][j]
    print(dist)
