import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')
def mergeSort(arr):
    invCount = 0
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        # # want to show the array split in tree diagram
        # print('L',L,'R',R)
        invCount += mergeSort(L)
        invCount += mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        print('L',L,'R',R)
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                invCount += mid - i # This is the only line that is different from mergeSort.py
                print((L[i],R[j])) 
                print('invCount',mid-i)
                # rest elements of left half are greater than R[j]
                # so no. of inversions = mid - i
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return invCount
        
       
def getInversions(arr,n) :
	# Write your code here.
	return mergeSort(arr)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int,input().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))

# input
# 3
# 3 2 1

# output
# 3


