# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


from collections import deque


class Solution:
    def topView(self, root):
        if not root:
            return []

        queue = deque([(root, 0)])
        mapping = {}

        while queue:
            curr, level = queue.popleft()

            if level not in mapping:
                mapping[level] = curr.data

            if curr.left:
                queue.append((curr.left, level - 1))
            if curr.right:
                queue.append((curr.right, level + 1))

        sorted_map = sorted(mapping.items())
        res = [v for k, v in sorted_map]
        return res
