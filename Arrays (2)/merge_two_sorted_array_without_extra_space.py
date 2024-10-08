# 1st Optimal Approach
import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # index of the last element in nums1
        j = n - 1  # index of the last element in nums2
        k = m + n - 1  # index of the last empty slot in nums1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # If there are any remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    arr1 = [1, 4, 8, 10, 0, 0, 0]
    arr2 = [2, 3, 9]
    m = 4
    n = 3
    sol = Solution()
    sol.merge(arr1, m, arr2, n)
    print(arr1)


# may be on GFG
# gap method -> 2nd Optimal Approach
# def swapIfGreater(arr1, arr2, ind1, ind2):
#     if arr1[ind1] > arr2[ind2]:
#         arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

# def merge(arr1, arr2, n, m):
#     # len of the imaginary single array:
#     len = n + m

#     # Initial gap:
#     # gap = (len // 2) + (len % 2)
#     gap = math.ceil(len/2)

#     while gap > 0:
#         # Place 2 pointers:
#         left = 0
#         right = left + gap
#         while right < len:
#             # case 1: left in arr1[]
#             # and right in arr2[]:
#             if left < n and right >= n:
#                 swapIfGreater(arr1, arr2, left, right - n)
#             # case 2: both pointers in arr2[]:
#             elif left >= n:
#                 swapIfGreater(arr2, arr2, left - n, right - n)
#             # case 3: both pointers in arr1[]:
#             else:
#                 swapIfGreater(arr1, arr1, left, right)
#             left += 1
#             right += 1
#         # break if iteration gap=1 is completed:
#         if gap == 1:
#             break
#         # Otherwise, calculate new gap:
#         # gap = (gap // 2) + (gap % 2)
#         gap = math.ceil(gap/2)


# if __name__ == '__main__':
#     arr1 = [1, 4, 8, 10]
#     arr2 = [2, 3, 9]
#     n = 4
#     m = 3
#     merge(arr1, arr2, n, m)

#     print("The merged arrays are:")
#     print("arr1[] = ", end="")
#     for i in range(n):
#         print(arr1[i], end=" ")
#     print("\narr2[] = ", end="")
#     for i in range(m):
#         print(arr2[i], end=" ")
#     print()

# Time Complexity: O((n+m)*log(n+m))
# Reason: The gap is ranging from n+m to 1 and
# every time the gap gets divided by 2. So, the time complexity of the outer loop will be O(log(n+m)).
# Now, for each value of the gap, the inner loop can at most run for (n+m) times.
# Space Complexity: O(1)
