dp = [[0 for i in range(1000)] for j in range(1000)]

def findLongestRepeatingSubSeq( X, m, n):
    
    if(dp[m][n]!=-1):
        return dp[m][n]

    if (m == 0 or n == 0):
        dp[m][n] = 0
        return dp[m][n]

    if (X[m - 1] == X[n - 1] and m != n):
        dp[m][n] = findLongestRepeatingSubSeq(X, 
                            m - 1, n - 1) + 1
        
        return dp[m][n]

    dp[m][n] = max (findLongestRepeatingSubSeq(X, m, n - 1), 
                        findLongestRepeatingSubSeq(X, m - 1, n))
    return dp[m][n]
