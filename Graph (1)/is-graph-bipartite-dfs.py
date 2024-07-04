# Linear graphs with no cycle are always bipartite graph
# Bipartite condition - can be divided into two sets such that no two nodes in the same set are connected
# In simpler terms - color the nodes with two colors such that no two adjacent nodes have the same color
# Any graph with even length cycle is bipartite
# Any graph with odd length cycle is not bipartite

from typing import List


class Solution:
    
    def dfs(self,src,parentColor,adj,colors):
        if(parentColor==-1):
            colors[src]=0
        else:
            colors[src]= not parentColor
        
        for adjacentNode in adj[src]:
            if colors[adjacentNode] == -1:
                if(not self.dfs(adjacentNode,colors[src],adj,colors)):
                    return False
            elif colors[adjacentNode]==colors[src]:
                return False
        return True
        
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        adj = graph

        colors = [-1]*V
        for i in range(V):
            if colors[i]==-1:
                if(self.dfs(i,-1,adj,colors)):
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
# graph = [[1],[],[3],[2]]

# failed test case
graph = [[2,3,5,6,7,8,9],[2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[1,2,3,6,9],[0,1,2,3,7,8,9],[0,1,2,3,4,7,8,9],[0,1,2,3,5,6,8,9],[0,1,2,3,5,6,7],[0,1,2,3,4,5,6,7]]

if(obj.isBipartite(graph)):
    print('1')
else:
    print('0')
                    