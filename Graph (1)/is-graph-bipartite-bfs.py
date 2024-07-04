# Linear graphs with no cycle are always bipartite graph
# Bipartite condition - can be divided into two sets such that no two nodes in the same set are connected
# In simpler terms - color the nodes with two colors such that no two adjacent nodes have the same color
# Any graph with even length cycle is bipartite
# Any graph with odd length cycle is not bipartite

from typing import List


class Solution:
    
    def bfs(self,src,adj,colors):
        colors[src]=0
        queue = [(src,0)]
                
        while queue:
            node, color = queue.pop(0)
            
            for adjacentNode in adj[node]:
                if colors[adjacentNode]==-1:
                    if color==0:
                        colors[adjacentNode]=1
                        queue.append((adjacentNode,1))
                    else:
                        colors[adjacentNode]=0
                        queue.append((adjacentNode,0))
                elif colors[adjacentNode]==color:
                    return False
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        adj = graph

        colors = [-1]*V
        for i in range(V):
            if colors[i]==-1:
                if(self.bfs(i,adj,colors)):
                    continue
                else:
                    return False
        return True
        
        

obj = Solution()

# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# graph = [[1,3],[0,2],[1,3],[0,2]]

# disconnected graph
# graph =  [[1],[],[3],[]]

# disconnected graph with even length cycle
graph = [[1],[],[3],[2]]

if(obj.isBipartite(graph)):
    print('1')
else:
    print('0')
                    