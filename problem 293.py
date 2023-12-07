class Solution:

    def DFSUtil(self,adj,v,visited,stack):

        visited[v] = True

        for i in adj[v]:

            if visited[i] == False:
                self.DFSUtil(adj,i,visited,stack)

        stack.insert(0,v)

    def topoSort(self, V, adj):

        visited = [False]*V
        stack =[]

        for i in range(V):

            if visited[i] == False:
                self.DFSUtil(adj,i,visited,stack)

        return stack
