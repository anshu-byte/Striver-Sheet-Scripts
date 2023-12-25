class Solution:
    def __init__(self):
        self.max_path_sum = float(-inf)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def preOrderTraversal(node):
            if not node:
                return 0

            left_path_sum = max(0, preOrderTraversal(node.left))
            right_path_sum = max(0, preOrderTraversal(node.right))

            self.max_path_sum = max(
                self.max_path_sum, node.val + left_path_sum + right_path_sum
            )

            return node.val + max(left_path_sum, right_path_sum)

        preOrderTraversal(root)
        return self.max_path_sum
