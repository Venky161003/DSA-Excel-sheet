dx = [-1, 0, 1]
dy = [-1, -1, -1]

def is_valid(x, y, n, m):
	if x >= 0 and x < n and y >= 0 and y < m:
		return True
	return False

def max_gold(n, m, M):

	dp = [[0 for j in range(m)] for i in range(n)]
	for i in range(n):
		dp[i][0] = M[i][0]

	for j in range(1, m):
		for i in range(n):
			mx = float('-inf')
			for k in range(3):
				x = i + dx[k]
				y = j + dy[k]
				if is_valid(x, y, n, m):
					mx = max(mx, dp[x][y] + M[i][j])
			dp[i][j] = mx
	ans = float('-inf')

	for i in range(n):
		ans = max(ans, dp[i][m - 1])
	return ans


# Driver code
n = 4
m = 4
gold = [
	[1, 3, 1, 5],
	[2, 2, 4, 1],
	[5, 0, 2, 3],
	[0, 6, 1, 2],
]

print("Max Amount of gold collected = ", max_gold(n, m, gold))
