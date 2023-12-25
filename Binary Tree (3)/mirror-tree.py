# User function Template for python3

"""
class Node:
    def _init_(self, data):
        self.right = None
        self.data = data
        self.left = None
"""


# your task is to complete this function
class Solution:
    def mirror(self, root):
        # Base case: if the tree is empty or a leaf node
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        return root
