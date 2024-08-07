def non_overlapping_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    cnt = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            cnt += 1
            end = intervals[i][1]
    return len(intervals) - cnt


if __name__ == "__main__":
    intervals = [[1, 4], [2, 5], [7, 9]]
    print(non_overlapping_intervals(intervals))
