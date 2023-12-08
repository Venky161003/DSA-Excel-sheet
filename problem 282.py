from queue import Queue
from typing import List
class Solution:

    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans = []

        vis = [False for i in range(V)]

        q = Queue(maxsize = 0)
        q.put(0)

        vis[0] = True
        
        while(q.empty() == False):

            v = q.get()
            ans.append(v)

            for i in adj[v]:

                if(vis[i] == False):
                    vis[i] = True
                    q.put(i)

        return ans
