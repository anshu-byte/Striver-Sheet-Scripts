from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)  # Convert wordDict to a set for faster lookup

        @lru_cache(maxsize=None)
        def solve(ind):
            if ind == n:
                return True
            for i in range(ind, n):
                sub = s[ind : i + 1]
                if sub in word_set:
                    if solve(i + 1):
                        return True
            return False

        return solve(0)
