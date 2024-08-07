from typing import List


class Solution:
    def __init__(self) -> None:
        self.stack = []

    def dfs(self, src, vis, adj):
        vis[src] = True
        for adjacentNode in adj[src]:
            if not vis[adjacentNode]:
                self.dfs(adjacentNode, vis, adj)
        self.stack.append(src)

    def topologicalSort(self, V, adj):
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, adj)
        self.stack.reverse()
        return self.stack

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])

        visited = [0] * numCourses  # 0: not visited, 1: visiting, 2: visited

        def dfs(node):
            if visited[node] == 1:
                return False  # Cycle detected
            if visited[node] == 2:
                return True  # Node already visited

            visited[node] = 1
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not self.canFinish(numCourses, prerequisites):
            return []
        adj_list = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])
        return self.topologicalSort(numCourses, adj_list)
