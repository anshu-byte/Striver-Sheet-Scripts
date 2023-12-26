from typing import List, Optional
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        leftToRight = True

        while queue:
            level_size = len(queue)
            current_level = [None] * level_size

            for i in range(level_size):
                node = queue.popleft()

                # Find position to fill node's value
                index = i if leftToRight else level_size - 1 - i
                current_level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            leftToRight = not leftToRight

        return result
