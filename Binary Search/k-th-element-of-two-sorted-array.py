class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)

        low, high = max(0, k - m), min(k, n)

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = k - partition_x

            max_left_x = float("-inf") if partition_x == 0 else arr1[partition_x - 1]
            min_right_x = float("inf") if partition_x == n else arr1[partition_x]

            max_left_y = float("-inf") if partition_y == 0 else arr2[partition_y - 1]
            min_right_y = float("inf") if partition_y == m else arr2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1
