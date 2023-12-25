import heapq
import random
from typing import List


class Solution:
    def quickSelect(
        self, nums: List[int], low: int, high: int, target_index: int
    ) -> int:
        if low == high:
            return nums[low]

        pivot_index = random.randint(low, high)
        nums[high], nums[pivot_index] = nums[pivot_index], nums[high]

        pivot, p = nums[high], low

        for i in range(low, high):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[p], nums[high] = nums[high], nums[p]

        if p == target_index:
            return nums[p]
        elif p < target_index:
            return self.quickSelect(nums, p + 1, high, target_index)
        else:
            return self.quickSelect(nums, low, p - 1, target_index)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This is correct solution for random array, leetcode added 41st testcase recently
        # It's not working on 41st test case
        # n = len(nums)
        # target_index = n - k
        # return self.quickSelect(nums, 0, n - 1, target_index)

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -heapq.heappop(max_heap)
