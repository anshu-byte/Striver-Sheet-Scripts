class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if len(arr) == 0:
                return None
            low, high = 0, len(arr) - 1
            mid = (low + high) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(arr[:mid])
            root.right = dfs(arr[mid + 1 :])
            return root

        return dfs(nums)
