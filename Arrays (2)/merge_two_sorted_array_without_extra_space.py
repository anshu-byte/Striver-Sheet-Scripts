# 1st Optimal Approach
import math
# def merge(arr1, arr2, n, m):

#     # Declare 2 pointers:
#     left = n - 1
#     right = 0

#     # Swap the elements until arr1[left] is smaller than arr2[right]:
#     while left >= 0 and right < m:
#         if arr1[left] > arr2[right]:
#             arr1[left], arr2[right] = arr2[right], arr1[left]
#             left -= 1
#             right += 1
#         else:
#             break

#     # Sort arr1[] and arr2[] individually:
#     arr1.sort()
#     arr2.sort()

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

# Time Complexity: O(min(n, m)) + O(n*logn) + O(m*logm)
# Space Complexity: O(1)

# gap method -> 2nd Optimal Approach
def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def merge(arr1, arr2, n, m):
    # len of the imaginary single array:
    len = n + m

    # Initial gap:
    # gap = (len // 2) + (len % 2)
    gap = math.ceil(len/2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < len:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        # gap = (gap // 2) + (gap % 2)
        gap = math.ceil(gap/2)


if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    merge(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print()

# Time Complexity: O((n+m)*log(n+m))
# Reason: The gap is ranging from n+m to 1 and 
# every time the gap gets divided by 2. So, the time complexity of the outer loop will be O(log(n+m)). 
# Now, for each value of the gap, the inner loop can at most run for (n+m) times. 
# Space Complexity: O(1)