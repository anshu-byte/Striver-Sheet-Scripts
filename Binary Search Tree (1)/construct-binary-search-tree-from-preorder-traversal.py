class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # def buildBST(pre):
        #     if len(pre)==0:
        #         return None
        #     root = TreeNode(pre[0])
        #     indx = 0
        #     for i in range(1,len(pre)):
        #         if pre[i]<pre[0]:
        #             indx = i
        #     root.left = buildBST(pre[1:indx+1])
        #     root.right = buildBST(pre[indx+1:])
        #     return root
        # return buildBST(preorder)

        def buildBST(low, high):
            if low >= high:
                return None
            root = TreeNode(preorder[low])
            indx = low
            for i in range(low + 1, high):
                if preorder[i] < preorder[low]:
                    indx = i
            root.left = buildBST(low + 1, indx + 1)
            root.right = buildBST(indx + 1, high)
            return root

        return buildBST(0, len(preorder))
