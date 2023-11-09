#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [-1]*V

    def isSafe(node, col):
        for i in range(V):
            if graph[node][i] == 1 and color[i] == col:
                return False
        return True

    def solve(node):
        if node == V:
            return True
        for col in range(k):
            if isSafe(node, col):
                color[node] = col
                if solve(node + 1):
                    return True
                color[node] = -1
        return False

    return solve(0)

        