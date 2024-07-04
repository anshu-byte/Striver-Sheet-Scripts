# Use it when you have a directed acyclic graph (DAG)

class Solution:
    def __init__(self) -> None:
        self.stack = []
    def dfs(self,src,vis,adj):
        vis[src]=True
        for adjacentNode in adj[src]:
            if not vis[adjacentNode]:
                self.dfs(adjacentNode,vis,adj)
        self.stack.append(src)
        
    
    def topologicalSort(self,V,adj):
        vis = [False]*V
        for i in range(V):
            if not vis[i]:
                self.dfs(i,vis,adj)
        self.stack.reverse()
        return self.stack
if __name__ == "__main__":
    V = 6
    adj = [[],[],[3],[0,1],[0,2],[0,2]]
    obj = Solution()
    ans = obj.topologicalSort(V, adj)
    print(ans) # [5, 4, 2, 3, 1, 0]
