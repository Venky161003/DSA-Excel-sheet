class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
        #building table K[][] in bottom up manner.
        for i in range(n + 1):
            for w in range(W + 1):
                
                #building table K[][] in bottom up manner.
                if i == 0 or w == 0:
                    K[i][w] = 0
                    
                #if weight of current item is more than Knapsack capacity W
                #then this item cannot be included in the optimal solution.
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
                    
                #else updating K[i][w] as K[i-1][w].
                else:
                    K[i][w] = K[i - 1][w]
    
        #returning the result.
        return K[n][W]
