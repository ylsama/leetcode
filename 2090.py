"""
2090. K Radius Subarray Averages
"""
from math import trunc
from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1]*n
        firstSum = 0
        if k+1+k > n:
            return result

        for i in nums[:k+1+k]:
            firstSum += i

        for i in range(0+k, n-k):
            result[i] = trunc(firstSum/(1+k+k))
            if i+k+1 < n:
                firstSum -= nums[i-k]
                firstSum += nums[i+k+1]

        print(result)

        return result


def test():
    test = TestHelper()
    a = Solution()
    test.quickTest(a.getAverages, [[1], 0], [1])
    test.quickTest(a.getAverages, [[7, 4, 3, 9, 1, 8, 5, 2, 6], 3],
                   [-1, -1, -1, 5, 4, 4, -1, -1, -1])


if __name__ == "__main__":
    test()
