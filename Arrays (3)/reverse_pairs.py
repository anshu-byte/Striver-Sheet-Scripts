import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')
def mergeSort(arr):
    revPair = 0
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        revPair += mergeSort(L)
        revPair += mergeSort(R)

        i = j = k = 0
        
        # count Rev Pair
        for i in range(len(L)):
            while j < len(R) and L[i] > 2*R[j]:
                j += 1
            revPair += j
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
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
    return revPair
        
       
def getReversePairs(arr,n) :
	# Write your code here.
	return mergeSort(arr)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int,input().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getReversePairs(arr, n))

