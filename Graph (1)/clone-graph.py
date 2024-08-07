# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
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


if __name__ == "__main__":
    sol = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    print(sol.cloneGraph(node1))
