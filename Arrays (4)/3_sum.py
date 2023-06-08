from typing import List
class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        if len(nums) < 3:
            return arr
        nums.sort()

        for i in range(len(nums)-2):
            # avoid the duplicates while moving i:
            if (i==0 or nums[i-1] != nums[i]):
                l,r = i+1,len(nums)-1
                sum = target - nums[i]
                while(l<r):
                    if nums[l] + nums[r] == sum:
                        arr.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        # to avoid duplicates
                        while(l<r and nums[l] == nums[l-1]):
                            l += 1
                        while(l<r and nums[r] == nums[r+1]):
                            r -= 1
                    elif nums[l] + nums[r] < sum:
                        l += 1
                    else:
                        r -= 1
        return arr

sol = Solution()
nums = [2,7,7,11,4,1,7,7,15]
target = 16
print(sol.threeSum(nums, target))

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# generate three sum test case, where duplicates are allowed
# import random
# def generate_test_case(n):
#     arr = []
#     for i in range(n):
#         arr.append(random.randint(-100,100))
#     return arr

# arr = generate_test_case(100)
# target = random.randint(-100,100)
# print(arr)
# print(target)
# print(sol.threeSum(arr, target))