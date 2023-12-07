import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        visited=[[0]*len(grid[0]) for i in range(len(grid))]

        def isValid(x,y):
            if (x>=0 and x<n) and (y>=0 and y<m):
                return True
            return False

        def dfs(grid,x,y):
            visited[x][y]=1
            for i in [[-1,-1],[1,1],[1,0],[0,1],[1,-1],[-1,1],[-1,0],[0,-1]]:
                if isValid(x+i[0],y+i[1]) and visited[x+i[0]][y+i[1]]==0:
                    if grid[x+i[0]][y+i[1]]==1:
                        dfs(grid,x+i[0],y+i[1])
        
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]==1:
                    dfs(grid,i,j)
                    count+=1
        return count
