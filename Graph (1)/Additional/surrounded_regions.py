class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        if rows < 3 or cols < 3:
            return
        q = deque()

        for row in range(rows):
            q.append((row, 0))
            q.append((row, cols - 1))

        for col in range(1, cols - 1):
            q.append((0, col))
            q.append((rows - 1, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            row, col = q.popleft()

            if board[row][col] == "O":
                board[row][col] = "T"
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if not (0 <= new_row < rows and 0 <= new_col < cols):
                        continue
                    q.append((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
