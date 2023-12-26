class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.res = []

    def isLeaf(self, root):
        return root.left is None and root.right is None

    def leftBoundary(self, root):
        if root is None or self.isLeaf(root):
            return
        self.res.append(root.data)
        self.leftBoundary(root.left if root.left else root.right)

    def rightBoundary(self, root):
        if root is None or self.isLeaf(root):
            return
        self.rightBoundary(root.right if root.right else root.left)
        self.res.append(root.data)

    def leafNodes(self, root):
        if root is None:
            return
        self.leafNodes(root.left)
        if self.isLeaf(root):
            self.res.append(root.data)
        self.leafNodes(root.right)

    def printBoundaryView(self, root):
        # Code here
        if root is None:
            return
        self.res.append(root.data)
        self.leftBoundary(root.left)
        if not self.isLeaf(root):
            self.leafNodes(root)
        self.rightBoundary(root.right)
        return self.res
