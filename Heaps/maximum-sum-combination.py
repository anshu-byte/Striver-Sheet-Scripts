# User function Template for python3
import heapq


class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort()
        B.sort()

        heap = []

        # Initialize with the maximum sum combination and indices
        heapq.heappush(heap, (-(A[N - 1] + B[N - 1]), N - 1, N - 1))

        # Set to keep track of visited indices
        visited = set((N - 1, N - 1))

        # Result array to store maximum sum combinations
        result = []

        # Find K maximum sum combinations
        while K > 0:
            # Pop the maximum sum combination
            current_sum, i, j = heapq.heappop(heap)

            # Add the sum to the result array
            result.append(-current_sum)

            # Check and push the next possible sum combinations
            if i > 0 and (i - 1, j) not in visited:
                heapq.heappush(heap, (-(A[i - 1] + B[j]), i - 1, j))
                visited.add((i - 1, j))
            if j > 0 and (i, j - 1) not in visited:
                heapq.heappush(heap, (-(A[i] + B[j - 1]), i, j - 1))
                visited.add((i, j - 1))

            K -= 1

        return result
