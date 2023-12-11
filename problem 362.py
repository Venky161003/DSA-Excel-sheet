class Solution:

    def eggDrop(self,n, k):
        dp = []
        for i in range(n+1):
            temp = [-1]*(k+1)
            dp.append(temp)
            
        def solve(n,k):
            if n==0 or k==0:
                return 0
            if n==1:
                return k
            if k==1:
                return 1
            
            if dp[n][k] != -1:
                return dp[n][k]
            
            mn = float("inf")
            for i in range(1,k+1):
                tmp = max(solve(n-1,i-1), solve(n,k-i))
                if tmp<mn:
                    mn = tmp
            dp[n][k] = mn+1
            
            return dp[n][k]
        
        return solve(n,k)
