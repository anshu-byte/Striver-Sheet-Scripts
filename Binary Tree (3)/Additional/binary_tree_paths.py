from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def preOrder(node, path):
            if not node:
                return
            if not node.left and not node.right:
                paths.append("->".join(map(str, path + [node.val])))
                return
            path.append(node.val)
            preOrder(node.left, path)
            preOrder(node.right, path)
            path.pop()

        preOrder(root, [])
        return paths
