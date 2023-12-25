from collections import deque


class Solution:
    def __init__(self):
        self.zigzag = True

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([[1, root]])

        while queue:
            level, node = queue.popleft()
            if node:
                queue.append([level + 1, node.left])
                queue.append([level + 1, node.right])

                if level > len(res):
                    res.append(deque([node.val]))
                    self.zigzag = not self.zigzag

                else:
                    if self.zigzag:
                        res[level - 1].appendleft(node.val)
                    else:
                        res[level - 1].append(node.val)
        return res
