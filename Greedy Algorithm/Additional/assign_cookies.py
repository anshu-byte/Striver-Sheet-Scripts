from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        no_of_children = len(g)
        cookie_len = len(s)
        i, j = 0, 0
        while i < no_of_children and j < cookie_len:
            if g[i] <= s[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1
        return res
