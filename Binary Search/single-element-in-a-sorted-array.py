from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def isSingleElement(nums, mid):
            if mid == 0:
                return nums[mid] != nums[mid + 1]
            if mid == len(nums) - 1:
                return nums[mid] != nums[mid - 1]
            return nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]

        def findSingleElement(nums: List[int]) -> int:
            low, high = 0, len(nums) - 1

            while low < high:
                mid = low + (high - low) // 2

                if isSingleElement(nums, mid):
                    return nums[mid]

                if mid % 2 == 0:
                    if nums[mid] == nums[mid + 1]:
                        low = mid + 2
                    else:
                        high = mid
                else:
                    if nums[mid] == nums[mid - 1]:
                        low = mid + 1
                    else:
                        high = mid

            return nums[low]

        return findSingleElement(nums)
