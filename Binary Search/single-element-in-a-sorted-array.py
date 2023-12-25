from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def check(nums, mid):
            return (
                mid == 0
                and nums[mid] != nums[mid + 1]
                or mid == len(nums) - 1
                and nums[mid] != nums[mid - 1]
                or nums[mid] != nums[mid - 1]
                and nums[mid] != nums[mid + 1]
            )

        def singleElementInSortedArray(nums, n):
            if n == 1:
                return nums[0]
            low, high = 0, n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if check(nums, mid):
                    return nums[mid]
                elif mid % 2 == 0:
                    if nums[mid] == nums[mid + 1]:
                        low = mid + 2
                    else:
                        high = mid - 2
                else:
                    if nums[mid] == nums[mid - 1]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return nums[low]

        return singleElementInSortedArray(nums, len(nums))
