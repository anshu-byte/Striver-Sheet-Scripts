from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0, 0)])
        mapping = {}

        while queue:
            curr, vh, level = queue.popleft()

            if vh not in mapping:
                mapping[vh] = [(curr.val, level)]
            else:
                mapping[vh].append((curr.val, level))

            if curr.left:
                queue.append((curr.left, vh - 1, level + 1))
            if curr.right:
                queue.append((curr.right, vh + 1, level + 1))

        sorted_map = sorted(mapping.items())
        data = [v for k, v in sorted_map]
        res = [
            [x[0] for x in sorted(sub_list, key=lambda y: (y[1], y[0]))]
            for sub_list in data
        ]
        return res
