"""
1027. Longest Arithmetic Subsequence

Given an array nums of integers, return the length of the longest arithmetic
subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
(for 0 <= i < seq.length - 1).
"""
from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def findLongestArith(self, cache, nums, position, start, step):
        if (start, step) in cache:
            return cache[(start, step)]

        num = nums[start]
        nextNum = num + step

        if nextNum not in position:
            cache[(start, step)] = 1
            return 1

        nextBestPos = start
        for possible in position[nextNum]:
            if possible > start:
                nextBestPos = possible
                break

        if nextBestPos == start:
            cache[(start, step)] = 1
            return 1
        longest = self.findLongestArith(
            cache, nums, position, nextBestPos, step)

        cache[(start, step)] = longest + 1
        return longest + 1

    def longestArithSeqLength(self, nums: List[int]) -> int:
        position = {}
        for index, num in enumerate(nums):
            if num not in position:
                position[num] = []
            position[num].append(index)
        cache = {}

        longest = 2
        for index, num in enumerate(nums):
            for num2 in nums[index+1:]:
                step = num2 - num
                possibleResult = self.findLongestArith(
                    cache, nums, position, index, step)
                if longest < possibleResult:
                    longest = possibleResult
        return longest


def test():
    test = TestHelper()
    a = Solution()

    test.quickTest(a.longestArithSeqLength, [[3, 6, 9, 12]], 4)
    test.quickTest(a.longestArithSeqLength, [[9, 4, 7, 2, 10]], 3)
    test.quickTest(a.longestArithSeqLength, [[20, 1, 15, 3, 10, 5, 8]], 4)


if __name__ == "__main__":
    test()
