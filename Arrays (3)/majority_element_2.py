# Given an array of N integers, 
# write a program to return an element that occurs more than N/3 times in the given array.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        cnt1,cnt2 = 0,0
        el1,el2 = float('-inf'), float('-inf')
        for num in nums:
            if cnt1==0 and num!=el2:
                cnt1 = 1
                el1 = num
            elif cnt2==0 and num!=el1:
                cnt2 = 1
                el2 = num
            elif num==el1:
                cnt1 += 1
            elif num==el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1,cnt2 = 0,0
        for num in nums:
            if num==el1:
                cnt1+=1
            elif num==el2:
                cnt2+=1
        mini = int(len(nums) / 3) + 1
        if cnt1>=mini:
            res.append(el1)
        if cnt2>=mini:
            res.append(el2)
        return res