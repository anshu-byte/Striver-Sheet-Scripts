from collections import deque


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_and_depth(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0

            left_diameter, left_depth = diameter_and_depth(node.left)
            right_diameter, right_depth = diameter_and_depth(node.right)

            current_depth = max(left_depth, right_depth) + 1
            current_diameter = max(
                left_depth + right_depth, max(left_diameter, right_diameter)
            )

            return current_diameter, current_depth

        result, _ = diameter_and_depth(root)
        return result
