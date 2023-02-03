import sys

def mindist(dist, visited):
	min = inf
	for v in range(n):
		if(dist[v] < min and visited[v] == False):
			min = dist[v]
			index = v
	return index

def prims(graph):
	dist = [inf]*n
	parent = [None]*n
	dist[0] = 0
	visited = [False]*n
	parent[0] = -1 
	for j in range(n):
		x = mindist(dist, visited)
		visited[x] = True
		for i in range(n):
			if(graph[x][i] > 0 and visited[i] == False and dist[i] > graph[x][i]):
				dist[i] = graph[x][i]
				parent[i] = x
	for i in range(1,n):
		print(parent[i],i," - ",graph[i][parent[i]])

inf = sys.maxsize
graph = [#insert graph]
n = len(graph)

prims(graph)
