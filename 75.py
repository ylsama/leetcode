"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in
the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

You must solve this problem without using the library's sort function.

This could be a counted sort, as total are low
"""


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        allColors = [0, 1, 2]
        countedColorsAppearence = [0]*3

        for color in nums:
            countedColorsAppearence[color] += 1

        index = 0
        for color in allColors:
            for _ in range(countedColorsAppearence[color]):
                nums[index] = color
                index += 1
