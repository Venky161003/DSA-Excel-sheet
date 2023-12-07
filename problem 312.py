class Solution:
    def findOrder(self,alien_dict,n,k):
        graph = {chr(i+97):[] for i in range(k)} 
        
        for i in range(n-1):
            for j in range(min(len(alien_dict[i]),len(alien_dict[i+1]))):
                if alien_dict[i][j]!=alien_dict[i+1][j]:
                    graph[alien_dict[i][j]].append(alien_dict[i+1][j])
                    break

        stack = []
        visited = set()
        
        def dfs(c):
            if c in visited:
                return 
            visited.add(c)
            for adj in graph[c]:
                dfs(adj)
            stack.append(c)

        for c in graph:
            dfs(c)

        stack.reverse()   
        order = "".join(stack)
        return order 
