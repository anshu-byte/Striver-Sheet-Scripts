from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        if root:
            stack.append(root)

        while stack:
            current = stack.pop()
            result.append(current.val)

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)

        return result[::-1]
