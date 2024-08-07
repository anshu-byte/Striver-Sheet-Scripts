class Solution:
    class Meeting:
        def __init__(self, start, end, pos):
            self.start = start
            self.end = end
            self.pos = pos

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        meets = []
        for i in range(n):
            meets.append(self.Meeting(start[i], end[i], i))
        meets = sorted(meets, key=lambda x: (x.end, x.pos))
        res = 1
        limit = meets[0].end
        for i in range(1, n):
            if meets[i].start >= limit:
                res += 1
                limit = meets[i].end
        return res


sol = Solution()
n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(sol.maximumMeetings(n, start, end))
