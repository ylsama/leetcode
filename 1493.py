from ulti.testHelper.testHelper import TestHelper
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longestSubarray = 0
        last0 = -1
        curr0 = -1

        for index, value in enumerate(nums):
            if value == 0:
                last0 = curr0
                curr0 = index
            remember = 0
            if index >= curr0:
                remember = 1
            longestSubarray = max(longestSubarray, index - last0 - remember)

        return longestSubarray


def test():
    test = TestHelper()
    a = Solution()
    dir = "test/1493/"
    for fileName in ['1', '2', '3']:
        i, o = dir + fileName + '.inp', dir + fileName + '.out'
        test.fileTest(a.longestSubarray, i, o, 'test '+fileName)
    test.quickTest(a.longestSubarray, [[0, 0, 0]], 0)


if __name__ == "__main__":
    test()
