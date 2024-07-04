from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            adj_list[pair[0]].append(pair[1])

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
        
numCourses = 2
prerequisites = [[1,0],[0,1]]
s = Solution()
if(s.canFinish(numCourses,prerequisites)):
    print("Can finish")
else:
    print("Cannot finish")