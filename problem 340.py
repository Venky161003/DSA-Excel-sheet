class Solution:
    def longestSubsequence(self, N, A):

        lst=[1]*N

        for i in range(len(A)-1,-1,-1):
            for j in range(i+1,len(A)):

                if abs(A[i]-A[j])==1:
                    lst[i]=max(lst[i],1+lst[j])

        return max(lst)
