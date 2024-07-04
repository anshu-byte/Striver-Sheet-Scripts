# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self,node):
        if not node:
            return None
        visited = {}
        stack = [node]
        visited[node] = Node(node.val, [])
        while stack:
            s = stack.pop()
            for i in s.neighbors:
                if i not in visited:
                    visited[i] = Node(i.val, [])
                    stack.append(i)
                visited[s].neighbors.append(visited[i])
        return visited[node]
        