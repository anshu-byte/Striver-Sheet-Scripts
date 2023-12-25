from collections import deque


class Solution:
    def levelOrder(self, root):
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
                    res.append([node.val])
                else:
                    res[level - 1].append(node.val)

        return res
