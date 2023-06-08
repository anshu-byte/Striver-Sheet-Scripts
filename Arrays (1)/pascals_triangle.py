from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        for i in range(1,numRows):
            for j in range(i+1):
                if j==0:
                    l.append([1])
                elif j==i:
                    l[i].append(1)
                else:
                    l[i].append(l[i-1][j-1]+l[i-1][j])
        return l

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)