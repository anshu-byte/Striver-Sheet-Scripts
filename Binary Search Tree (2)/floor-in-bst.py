# User function Template for python3


class Solution:
    def floor(self, root, inp):
        # code here
        curr = root
        res = -1
        while curr:
            if curr.data == inp:
                res = inp
                break
            elif curr.data < inp:
                res = curr.data
                curr = curr.right
            else:
                curr = curr.left
        return res
