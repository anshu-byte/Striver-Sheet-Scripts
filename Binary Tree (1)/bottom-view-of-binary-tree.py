# User function Template for python3
from collections import deque


class Solution:
    def bottomView(self, root):
        q = deque()
        mapping = {}
        q.append((root, 0))

        while q:
            curr, level = q.popleft()
            mapping[level] = curr.data
            if curr.left:
                q.append((curr.left, level - 1))
            if curr.right:
                q.append((curr.right, level + 1))

        sorted_map = sorted(mapping.items())
        res = []
        for k, v in sorted_map:
            res.append(v)
        return res
