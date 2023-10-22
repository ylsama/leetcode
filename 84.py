"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""
from bisect import bisect_right
from typing import List

from ulti.testHelper.testHelper import TestHelper


class Solution:
    def largestRectangleArea_mine(self, heights: List[int]) -> int:
        cache = []
        keys = []
        largest = 0

        for i, h in enumerate(heights + [0]):
            if i == 0:
                h = heights[0]
                largest = h
                cache.append(i)
                keys.append(h)
                continue

            w = i
            while keys[-1] > h:
                k = keys.pop()
                start = cache.pop()
                if largest < (i-start)*k:
                    largest = (i-start)*k
                w = start

            if len(keys) == 0 or keys[-1] != h:
                keys.append(h)
                cache.append(w)

        return largest

    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        # stack = [<remember_height>, <window_length>]]
        stack = [[heights[0], 1]]
        topHeight, topWidth = stack[-1]
        largest = heights[0]

        for h in heights[1:] + [0]:
            w = 1
            if stack and h <= topHeight:
                while stack and h < topHeight:
                    currH, currW = stack.pop()
                    topHeight, topWidth = stack[-1] if stack else (None, None)
                    w += currW
                    area = (w - 1) * currH
                    if area > largest:
                        largest = area
                if stack and h == topHeight:
                    topWidth += w
                    stack[-1] = (h, topWidth)
                    continue
            topHeight, topWidth = h, w
            stack.append((topHeight, topWidth))
        return largest


def test():
    a = Solution()
    test = TestHelper()
    test.quickTest(a.largestRectangleArea, [
                   [2, 1, 5, 6, 2, 3]], 10, "Example 1")
    test.quickTest(a.largestRectangleArea, [[2, 4]], 4, "Example 2")


if __name__ == "__main__":
    test()
