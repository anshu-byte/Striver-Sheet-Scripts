class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        split_indx = inorder.index(root_val)

        left_inorder = inorder[:split_indx]
        right_inorder = inorder[split_indx + 1 :]

        left_preorder = preorder[1 : 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder) :]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
