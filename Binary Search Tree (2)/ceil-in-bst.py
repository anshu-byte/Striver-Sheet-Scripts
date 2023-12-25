# Function to return the ceil of given number in BST.


class Solution:
    def findCeil(self, root, inp):
        # code here
        curr = root
        res = -1
        while curr:
            if curr.key == inp:
                res = inp
                break
            elif curr.key < inp:
                curr = curr.right
            else:
                res = curr.key
                curr = curr.left
        return res
