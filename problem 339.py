def maxSumPairWithDifferenceLessThanK(arr, N, K):

	arr.sort()

	dp = [0] * N

	dp[0] = 0

	for i in range(1, N):

		dp[i] = dp[i-1]

		if (arr[i] - arr[i-1] < K):

			if (i >= 2):
				dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]);
			else:
				dp[i] = max(dp[i], arr[i] + arr[i-1]);

	return dp[N - 1]

# Driver code 
arr = [3, 5, 10, 15, 17, 12, 9]
N = len(arr)
K = 4
print(maxSumPairWithDifferenceLessThanK(arr, N, K))
