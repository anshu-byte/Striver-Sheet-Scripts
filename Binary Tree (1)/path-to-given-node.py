# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        def find_path(node, target, current_path, result):
            if not node:
                return

            # Add the current node to the path
            current_path.append(node.val)

            # Check if the current node is the target
            if node.val == target:
                result.extend(current_path)
                return

            find_path(node.left, target, current_path.copy(), result)
            find_path(node.right, target, current_path.copy(), result)

        result = []
        find_path(A, B, [], result)
        return result
