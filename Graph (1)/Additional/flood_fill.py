class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        queue = deque([(sr, sc)])
        rows, cols = len(image), len(image[0])

        if image[sr][sc] == new_color:
            return image

        old_color = image[sr][sc]

        while queue:
            x, y = queue.popleft()

            if image[x][y] == old_color:
                image[x][y] = new_color
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue

                    if image[xx][yy] == old_color:
                        queue.append((xx, yy))
        return image
