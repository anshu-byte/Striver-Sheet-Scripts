from collections import deque


class Solution:
    def widthOfBinaryTree(self, root):
        max_width = 0
        q = deque([(0, root)])

        while q:
            level_size = len(q)
            min_no_nodes = q[0][0]
            first, last = 0, 0
            for i in range(level_size):
                level, node = q.popleft()
                level -= min_no_nodes
                if i == 0:
                    first = level
                if i == level_size - 1:
                    last = level
                if node.left:
                    q.append([2 * level + 1, node.left])
                if node.right:
                    q.append([2 * level + 2, node.right])
            max_width = max(max_width, last - first + 1)
        return max_width
