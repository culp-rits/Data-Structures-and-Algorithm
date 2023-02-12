def bfs(graph,visited):
    x = q.pop(0)
    visited.append(x)
    for i in graph[x]:
        if(i not in visited):
            q.append(x)
    if(visited.size()!=n):
        bfs(graph,visited)
q=[]
visited=[]
