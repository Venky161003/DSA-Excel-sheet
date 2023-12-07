class Solution:
    def isNegativeWeightCycle(self, n, edges):
        inf = 1000000000000000000 
        d = [0 for i in range(n)] 
        p = [-1 for i in range(n)] 
        for i in range(n): 
            x = -1 
            for e in edges:
                if(d[e[0]] + e[2] < d[e[1]]):
                    d[e[1]] = d[e[0]] + e[2] 
                    p[e[1]] = e[0] 
                    x = e[1] 
        if(x == -1):
            return 0
        return 1 
