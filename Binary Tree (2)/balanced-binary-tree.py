class Solution:
    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
