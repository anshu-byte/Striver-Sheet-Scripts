from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        res = list(sorted_d.keys())[:k]
        return res
