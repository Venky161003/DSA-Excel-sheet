def isNegCycleBellmanFord(src, dist):
	global graph, V, E

	for i in range(V):
		dist[i] = 10**18
	dist[src] = 0

	for i in range(1, V):
		for j in range(E):
			u = graph[j][0]
			v = graph[j][1]
			weight = graph[j][2]
			if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
				dist[v] = dist[u] + weight

	for i in range(E):
		u = graph[i][0]
		v = graph[i][1]
		weight = graph[i][2]
		if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
			return True

	return False

def isNegCycleDisconnected():
	global V, E, graph

	visited = [0]*V

	dist = [0]*V

	for i in range(V):
		if (visited[i] == 0):

			if (isNegCycleBellmanFord(i, dist)):
				return True

			for i in range(V):
				if (dist[i] != 10**18):
					visited[i] = True
	return False


#Driver code
if __name__ == '__main__':

	V = 5 
	E = 8 
	graph = [[0, 0, 0] for i in range(8)]

	graph[0][0] = 0
	graph[0][1] = 1
	graph[0][2] = -1

	graph[1][0] = 0
	graph[1][1] = 2
	graph[1][2] = 4

	graph[2][0] = 1
	graph[2][1] = 2
	graph[2][2] = 3

	graph[3][0] = 1
	graph[3][1] = 3
	graph[3][2] = 2

	graph[4][0] = 1
	graph[4][1] = 4
	graph[4][2] = 2

	graph[5][0] = 3
	graph[5][1] = 2
	graph[5][2] = 5

	graph[6][0] = 3
	graph[6][1] = 1
	graph[6][2] = 1

	graph[7][0] = 4
	graph[7][1] = 3
	graph[7][2] = -3

	if (isNegCycleDisconnected()):
		print("Yes")
	else:
		print("No")

