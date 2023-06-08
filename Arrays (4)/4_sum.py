from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        if len(nums) < 3:
            return arr
        nums.sort()
        for i in range(len(nums)-3):
            # avoid the duplicates while moving i:
            if (i==0 or nums[i-1] != nums[i]):
                for j in range(i+1,len(nums)-2):
                    # avoid the duplicates while moving j:
                    if (j==i+1 or nums[j-1] != nums[j]):
                        l,r = j+1,len(nums)-1
                        sum = target - nums[i] - nums[j]
                        while(l<r):
                            if nums[l] + nums[r] == sum:
                                arr.append([nums[i],nums[j],nums[l],nums[r]])
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

# Time Complexity: O(n^3)
# Space Complexity: O(n)

sol = Solution()
nums = [2,7,7,11,4,1,7,7,15]
target = 32
print(sol.fourSum(nums, target))

