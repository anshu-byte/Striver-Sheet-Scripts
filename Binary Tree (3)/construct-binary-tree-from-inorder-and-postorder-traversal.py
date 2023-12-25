class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        split_index = inorder.index(root_val)

        left_inorder = inorder[:split_index]
        right_inorder = inorder[split_index + 1 :]

        root.right = self.buildTree(right_inorder, postorder)
        root.left = self.buildTree(left_inorder, postorder)

        return root
