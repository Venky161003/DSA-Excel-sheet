class Solution:

    def countPS(self,s):

        t = [[-1 for i in range(1001)]for i in range(1001)]
        mod = 10**9+7

        def solve(s,i,j,t):

            if i==j:
                return 1
            if i>j:
                return 0

            if t[i][j]!=-1:
                return t[i][j]

            elif s[i]==s[j]:

                t[i][j] = 1 + solve(s,i+1,j,t)%mod + solve(s,i,j-1,t)%mod
                t[i][j] %= mod
                return t[i][j]

            else:

                t[i][j] = solve(s,i+1,j,t)%mod + solve(s,i,j-1,t)%mod - solve(s,i+1,j-1,t)%mod
                t[i][j] %= mod
                return t[i][j]

        return solve(s,0,len(s)-1,t)
