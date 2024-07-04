# Use it when you have a directed acyclic graph (DAG)
# In degree -> No. of incoming edges to a node
class Solution:
    def topologicalSort(self,V,adj):
        inDegree = [0]*V
        for i in range(V):
            for adjacentNode in adj[i]:
                inDegree[adjacentNode] += 1
        queue = []
        for i in range(V):
            if inDegree[i]==0:
                queue.append(i)
        while(queue):
            node  = queue.pop(0)
            print(node)
            for adjacentNode in adj[node]:
                inDegree[adjacentNode]-=1
                if(inDegree[adjacentNode]==0):
                    queue.append(adjacentNode)

            
if __name__== "__main__":
    V = 4
    adj = [[1],[2],[],[1,2]]
    obj = Solution()
    obj.topologicalSort(V,adj)
    