class Solution:
    def maxChainLen(self,Parr, n):

        prev = -1e9
        ans = 0
        Parr = sorted(Parr, key = lambda x: x.b)
        for i in range(n):
            if (Parr[i].a > prev):
                prev = Parr[i].b
                ans += 1
        return ans
