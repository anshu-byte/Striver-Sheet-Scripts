class Solution:
    def __init__(self):
        self.ans = True

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def func(node):
            if node and not node.left and not node.right:
                return node.val

            left_sum = func(node.left)
            right_sum = func(node.right)

            if left_sum + right_sum != node.val:
                self.ans = False
            return node.val + left_sum + right_sum

        func(root)
        return self.ans
