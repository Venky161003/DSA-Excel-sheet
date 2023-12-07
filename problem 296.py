from collections import deque


class Solution:

	def canFinish(self, numTasks, prerequisites):
		graph = [[] for _ in range(numTasks)]
		inDegree = [0] * numTasks

		for edge in prerequisites:
			graph[edge[0]].append(edge[1])
			inDegree[edge[1]] += 1

		queue = deque()

		for i in range(numTasks):
			if inDegree[i] == 0:
				queue.append(i)

		while queue:
			node = queue.popleft()

			for neighbor in graph[node]:
				inDegree[neighbor] -= 1

				if inDegree[neighbor] == 0:
					queue.append(neighbor)

		for i in range(numTasks):
			if inDegree[i] != 0:
				return False

		return True


#Driver code
numTasks = 4
prerequisites = [
	[1, 0],
	[2, 1],
	[3, 2]
]

solution = Solution()
if solution.canFinish(numTasks, prerequisites):
	print("Possible to finish all tasks")
else:
	print("Impossible to finish all tasks")
