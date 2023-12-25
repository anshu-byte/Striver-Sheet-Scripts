class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def binary_search(node):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val < val:
                return binary_search(node.right)
            else:
                return binary_search(node.left)

        return binary_search(root)
