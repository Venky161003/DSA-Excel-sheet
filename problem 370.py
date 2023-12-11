def longestPalinSubseq(S):
	R = S[::-1]

	dp = [[0] * (len(R) + 1) for _ in range(len(S) + 1)]

	for i in range(1, len(S) + 1):
		for j in range(1, len(R) + 1):
			if S[i - 1] == R[j - 1]:
				dp[i][j] = 1 + dp[i - 1][j - 1]
			else:
				dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

	return dp[len(S)][len(R)]


# Driver code
s = "GEEKSFORGEEKS"
print("The length of the LPS is", longestPalinSubseq(s))

