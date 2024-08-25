from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n < 4:
            return []

        def canPlace(mat, row, col):
            for r in range(row):
                if mat[r][col] == "Q":
                    return False

            for c in range(col):
                if mat[row][c] == "Q":
                    return False

            dx, dy = row - 1, col - 1
            while dx >= 0 and dy >= 0:
                if mat[dx][dy] == "Q":
                    return False
                dx -= 1
                dy -= 1

            dx, dy = row - 1, col + 1
            while dx >= 0 and dy < n:
                if mat[dx][dy] == "Q":
                    return False
                dx -= 1
                dy += 1

            return True

        temp = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def dfs(row, cnt, matrix):
            if row == n:
                if cnt == n:
                    new_matrix = ["".join(row) for row in matrix]
                    res.append(new_matrix)
                return

            for col in range(n):
                if canPlace(matrix, row, col):
                    matrix[row][col] = "Q"
                    dfs(row + 1, cnt + 1, matrix)
                    matrix[row][col] = "."

        dfs(0, 0, temp)
        return res
