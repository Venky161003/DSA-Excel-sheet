def optCost_memoized(freq, i, j):

	if cost[i][j]:
		return cost[i][j]

	fsum = Sum(freq, i, j)

	Min = 999999999999

	for r in range(i, j + 1):
		c = (optCost_memoized(freq, i, r - 1) + optCost_memoized(freq, r + 1, j))
		c += fsum
		if c < Min:
			Min = c
			cost[i][j] = c

	return cost[i][j]

def optimalSearchTree(keys, freq, n):

	return optCost_memoized(freq, 0, n - 1)

def Sum(freq, i, j):
	s = 0
	for k in range(i, j + 1):
		s += freq[k]
	return s


if __name__ == '__main__':
	keys = [10, 12, 20]
	freq = [34, 8, 50]
	n = len(keys)

	cost = [[0 for x in range(n+1)] for y in range(n+1)]

	for i in range(n):
		cost[i][i] = freq[i]

	print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))
