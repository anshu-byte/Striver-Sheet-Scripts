from collections import deque


class Solution:
    def widthOfBinaryTree(self, root):
        level_old, num_old, max_width = 1, 1, 0
        queue = deque([[level_old, num_old, root]])

        while queue:
            level, num, node = queue.popleft()
            if node:
                queue.append([level + 1, 2 * num, node.left])
                queue.append([level + 1, 2 * num + 1, node.right])
                if level == level_old:
                    max_width = max(max_width, num - num_old + 1)
                else:
                    level_old, num_old = level, num
        return max_width
