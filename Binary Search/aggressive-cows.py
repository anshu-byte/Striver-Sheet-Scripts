# User function Template for python3


class Solution:
    def check(self, n, k, stalls, mid):
        noOfCows = 1
        prevStall = stalls[0]
        for i in range(1, n):
            if stalls[i] - prevStall >= mid:
                noOfCows += 1
                if noOfCows == k:
                    return True
                prevStall = stalls[i]
        return False

    def solve(self, n, k, stalls):
        stalls.sort()
        low = 0
        high = stalls[n - 1] - stalls[0]

        while low <= high:
            mid = (low + high + 1) // 2
            if self.check(n, k, stalls, mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
