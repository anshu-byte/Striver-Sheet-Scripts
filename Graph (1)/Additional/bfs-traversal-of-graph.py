class Graph: 
    def __init__(self,V): 
        self.V = V     
        self.adj = [[] for i in range(V)]

    def addEdge(self,v, w):    
        self.adj[v].append(w) 

    def BFS(self, s):
        visited = [False for i in range(self.V)]
        
        queue = []
        queue.append(s)
        
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            
            for node in self.adj[s]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0); 
    g.addEdge(0, 2); 
    g.addEdge(2, 1); 
    g.addEdge(0, 3); 
    g.addEdge(1, 4); 

    print("Following is Breadth First Traversal from vertex 0:", end=" ")
    g.BFS(0)
    
    # Following is Breadth First Traversal from vertex 0: 0 2 3 1 4 
    