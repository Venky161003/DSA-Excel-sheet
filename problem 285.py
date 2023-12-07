def countTriangle(g, isDirected):
	nodes = len(g)
	count_Triangle = 0

	for i in range(nodes):
		for j in range(nodes):
			for k in range(nodes):

				if(i != j and i != k
				and j != k and
				g[i][j] and g[j][k] 
				and g[k][i]):
					count_Triangle += 1

	if isDirected:
	return count_Triangle//3
	else: return count_Triangle//6

graph = [[0, 1, 1, 0],
		[1, 0, 1, 1],
		[1, 1, 0, 1],
		[0, 1, 1, 0]]

digraph = [[0, 0, 1, 0],
		[1, 0, 0, 1],
		[0, 1, 0, 0],
		[0, 0, 1, 0]]

print("The Number of triangles in undirected graph : %d" %
	countTriangle(graph, False))

print("The Number of triangles in directed graph : %d" %
	countTriangle(digraph, True))
