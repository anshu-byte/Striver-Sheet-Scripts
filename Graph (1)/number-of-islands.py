from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        queue = []
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    if visited[i][j]:
                        continue
                    result+=1
                    queue.append((i,j))
                    visited[i][j] = True
                    
                    while queue:
                        r, c = queue.pop(0)
                        for direction in directions:
                            newRow, newCol = r+direction[0], c+direction[1]
                            if 0<=newRow<row and 0<=newCol<col and grid[newRow][newCol]=="1" and not visited[newRow][newCol]:
                                queue.append((newRow,newCol))
                                visited[newRow][newCol] = True
                            
        return result
                                
                        
                        
        
        