from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            curr_start,curr_stop = intervals[i][0],intervals[i][1]
            if len(res)==0:
                res.append([curr_start,curr_stop])
            else:
                last_pair = res[-1]
                last_start,last_stop = last_pair[0],last_pair[1]
                if curr_start<=last_stop:
                    res[-1] = [last_start,max(curr_stop,last_stop)]
                else:
                    res.append([curr_start,curr_stop])
        return res

# Time Complexity: O(nlogn) + O(n)
# Space Complexity: O(n)