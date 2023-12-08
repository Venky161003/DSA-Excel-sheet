def count(n):
    ways = [3,5,10]  
    return solve(ways,3,n) 

def solve(ways,n,target):
    if(target==0):   
        return (1)
    if(n==0): 
        return (0)
    if(ways[n-1]<=target):
        
        return solve(ways,n,target-ways[n-1])+solve(ways,n-1,target)
    else:
        return solve(ways,n-1,target) 
