# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    res = []

    def func(curr, level, res):
        if curr is None:
            return
        if len(res) == level:
            res.append(curr.data)
        func(curr.left, level + 1, res)
        func(curr.right, level + 1, res)

    func(root, 0, res)
    return res
