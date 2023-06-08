from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(1,rows):
            for c in range(r):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
        for row in range(rows):
            matrix[row] = matrix[row][::-1]
        
# Time Complexity: O(n^2)
# Space Complexity: O(1)
