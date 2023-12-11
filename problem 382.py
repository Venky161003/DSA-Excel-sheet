import sys

def f(idx, buy, prices, dp, cap, n):
	if cap == 0:
		return 0
	if idx == n:
		return 0
	if dp[idx][buy][cap] != -1:
		return dp[idx][buy][cap]

	profit = 0

	if buy == 0:
		dp[idx][buy][cap] = profit = max(-prices[idx] + f(idx + 1, 1, prices, dp, cap, n), f(idx + 1, 0, prices, dp, cap, n))

	else:
		dp[idx][buy][cap] = profit = max(prices[idx] + f(idx + 1, 0, prices, dp, cap - 1, n), f(idx + 1, 1, prices, dp, cap, n))

	return profit

def maxtwobuysell(prices, n):
	dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
	return f(0, 0, prices, dp, 2, n)

if __name__ == "__main__":
	arr = [2, 30, 15, 10, 8, 25, 80]
	size = len(arr)
	print(maxtwobuysell(arr, size))
