class Solution:

    def detect(self, node, adj, vis, dfsVis):
        vis[node] = True
        dfsVis[node] = True
        
        for adjacentNode in adj[node]:
            if not vis[adjacentNode]:
                if (self.detect(adjacentNode,adj,vis,dfsVis)):
                    return True
            elif dfsVis[adjacentNode]:
                return True
        dfsVis[node] = False
        return False
            
        
    
    def isCycle(self, V, adj):
        vis = [False] * V
        dfsVis = [False] * V
        for i in range(V):
            if not vis[i]:
                if self.detect(i, adj, vis, dfsVis):
                    return True
        return False

if __name__ == "__main__":
    V = 4
    # Adjacency list for cyclic directed graph
    adj = {0: [1], 1: [2], 2: [3], 3: [1]}
    
    # Adjacency list for acyclic directed graph
    # adj = {0: [1], 1: [2], 2: [3], 3:[]}
    obj = Solution()
    ans = obj.isCycle(V, adj)
    print("1" if ans else "0")
