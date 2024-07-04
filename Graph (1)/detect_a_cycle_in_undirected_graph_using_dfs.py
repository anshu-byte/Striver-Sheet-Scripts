class Solution:
    def detect(self, src, adj, vis):
        stack = [(src, -1)]
        
        while stack:
            node, parent = stack.pop()
            
            if not vis[node]:
                vis[node] = True

                for adjacentNode in adj[node]:
                    if not vis[adjacentNode]:
                        stack.append((adjacentNode, node))
                    elif adjacentNode != parent:
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
