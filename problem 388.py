class Solution:
    def setBits(self, N):
        cnt = 0 

        while N>0:

            if (N & 1) :
                cnt+=1

            N>>=1

        return cnt
