class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            return helper(node.right, val, upper) and helper(node.left, lower, val)

        return helper(root)
