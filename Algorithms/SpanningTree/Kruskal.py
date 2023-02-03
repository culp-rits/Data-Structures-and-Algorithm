def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
        parent[y] = x

def kruskal(graph):
    result=[]
    graph=sorted(graph, key=lambda item: item[2])
    parent=[i for i in range(n)]
    for i in graph:
        u,v,w = i
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append([u, v, w])
            union(parent, x, y)
    for u, v, w in result:
        print(u,v,w)

n = 6
graph = [#insert graph here]

kruskal(graph)
