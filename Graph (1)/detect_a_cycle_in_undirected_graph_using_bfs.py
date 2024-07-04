from collections import deque

class Solution:
    def detect(self, src, adj, vis):
        vis[src] = True
        q = deque([(src, -1)]) 
        
        while q:
            node, parent = q.popleft()
            
            for adjacentNode in adj[node]:
                if not vis[adjacentNode]:
                    vis[adjacentNode] = True
                    q.append((adjacentNode, node))
                elif parent != adjacentNode:
                    return True
        return False

    def isCycle(self, V, adj):
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                if self.detect(i, adj, vis):
                    return True
        return False

if __name__ == "__main__":
    V = 4
    adj = [[], [2], [1, 3], [2]]
    obj = Solution()
    ans = obj.isCycle(V, adj)
    print("1" if ans else "0")
