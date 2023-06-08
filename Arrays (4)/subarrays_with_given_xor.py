from collections import defaultdict


class Soution:
    def naiveSolve(self, A, B):
        res = 0
        n = len(A)
        for i in range(n):
            for j in range(i,n):
                xor = 0
                for _ in range(i,j+1):
                    xor ^= A[_]
                if xor == B:
                    res += 1
        return res
    # time complexity: O(n^3)
    # space complexity: O(1)

    def betterSolve(self, A, B):
        res = 0
        n = len(A)
        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor ^= A[j]
                if xor == B:
                    res += 1
        return res
    # time complexity: O(n^2)
    # space complexity: O(1)

    def optimalSolve(self, A,B):
        res = 0
        n = len(A)
        d = {}
        d[0] = 1
        xor = 0
        for i in range(n):
            # prefix XOR till index i:
            xor ^= A[i]
            # By formula: x = xr^k:
            x = xor ^ B

            # add the occurrence of xr^k
            # to the res:
            res += d.get(x, 0)
            # Insert the prefix xor till index i
            # into the dictionary:
            d[xor] = d.get(xor, 0) + 1

            # alternative without d.get(x, 0):
            # if x in d:
            #     res += d[x]
            # if xor in d:
            #     d[xor] += 1
            # else:
            #     d[xor] = 1
        return res
    

sol = Soution()
A = [4, 2, 2, 6, 4]
B = 6
print(sol.optimalSolve(A, B))

# what is subarray?
# subarray is a contiguous part of an array
# subarray is a part of an array

            






        
