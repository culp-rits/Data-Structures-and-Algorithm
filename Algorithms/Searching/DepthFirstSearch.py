def dfs(graph,visited,stack):
    x = stack.pop()
    print(x)
    visited[x] = True
    for i in range(n):
        if(graph[x][i] > 0 and visited[i] == False):
            stack.append(i)
            dfs(graph,visited,stack)
