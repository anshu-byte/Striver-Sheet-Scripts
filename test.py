# m = 3
# n = 4
# K = [[0 for i in range(n)]for i in range(m)]
# print(K)
# import sys
# # set output.txt location as it is outside the current directory
# sys.stdout = open('./output.txt', 'w')
# sys.stdin = open('./input.txt', 'r')

# t = int(input())
# # print(t)
# # nums = [5,2,6,1]
# # enum = list(enumerate(nums)) 
# # print(enum)

# # write code to generate all subarrays
# for i in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(arr)
#     # write code to generate all subarrays
#     for i in range(n):
#         for j in range(i+1,n+1):
#             print(arr[i:j])
#             # print(arr[i:j], end = " ")
#     print()
d = {}
d[0] = 1
print(d.get(0, 0))
# what is d.get(0, 0) ?
# d.get(0, 0) returns the value of key 0 if it exists in the dictionary d, otherwise it returns 0


