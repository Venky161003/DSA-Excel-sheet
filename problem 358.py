import sys
sys.setrecursionlimit(10500)
class Solution:

    def maximizeTheCuts(self, l, p, q, r): 

        dp = [-1]*(l + 1)  
      
        dp[0] = 0
      
        for i in range( l+1) : 

            if (dp[i] == -1): 
                continue

            if (i + p <= l): 
                dp[i + p] = (max(dp[i + p],  
                            dp[i] + 1)) 
      
           
            if (i + q <= l): 
                dp[i + q] = (max(dp[i + q],  
                            dp[i] + 1)) 
      
            
            if (i + r <= l): 
                dp[i + r] = (max(dp[i + r], 
                            dp[i] + 1)) 

        if(dp[l]==-1):
            return 0

        return dp[l] 
