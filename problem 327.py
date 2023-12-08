from collections import defaultdict

class Solution:

    def Anagrams(self, s, n):

        d=defaultdict(list)

        for i,e in enumerate(s):

            e=str(sorted(e))

            d[e].append(s[i])

        res=[]

        for l in d.values():

            res.append(l)

        return res
