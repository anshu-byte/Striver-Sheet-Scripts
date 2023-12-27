def changeTree(root):
    def helper(node, max_data):
        if not node:
            return 0

        node.data = max(node.data, max_data)
        left_sum = helper(node.left, node.data)
        right_sum = helper(node.right, node.data)
        node.data = max(node.data, left_sum + right_sum)
        return node.data

    if root:
        helper(root, root.data)
