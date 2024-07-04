# In degree -> No. of incoming edges to a node
class Solution:
    def __init__(self) -> None:
        self.size = 0
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
            self.size+=1
            for adjacentNode in adj[node]:
                inDegree[adjacentNode]-=1
                if(inDegree[adjacentNode]==0):
                    queue.append(adjacentNode)
        if self.size!=V:
            print("Cycle exists")

            
if __name__== "__main__":
    V = 4
    # adjacent list acyclic directed graph
    # adj = [[1],[2],[],[1,2]]
    
    # adjacent list cyclic directed graph
    adj = [[1],[2],[3],[0]]
    obj = Solution()
    obj.topologicalSort(V,adj)
    