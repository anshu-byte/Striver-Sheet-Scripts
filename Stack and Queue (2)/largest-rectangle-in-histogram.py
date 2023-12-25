from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smaller = [n] * n
        previous_smaller = [-1] * n

        stack = []

        for i in range(n):
            height = heights[i]

            while stack and heights[stack[-1]] > height:
                next_smaller[stack.pop()] = i
            if stack:
                previous_smaller[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(n):
            current_height = heights[i]
            width = next_smaller[i] - previous_smaller[i] - 1
            max_area = max(max_area, current_height * width)
        return max_area
