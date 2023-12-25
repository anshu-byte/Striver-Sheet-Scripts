from collections import deque
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = deque()
        d = {}
        n = len(nums2)
        for i in range(n):
            num = nums2[n - 1 - i]
            while s and s[-1] < num:
                s.pop()
            d[num] = -1 if not s else s[-1]
            s.append(num)
        return [d[num] for num in nums1]
