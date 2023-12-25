# User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


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


# {
# Driver Code Starts
# Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
# {
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)


# {
# Driver Code Starts
# Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
# {
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
# Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]
