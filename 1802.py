"""
1802. Maximum Value at a Given Index in a Bounded Array

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

-   `1 <= n <= maxSum <= 10**9`
-   `0 <= index < n`
"""
from ulti.test.testHelper import Test
from math import log, trunc


class Solution:
    def caculate1_n(self, n):
        return (n+1)*n // 2

    def rangeLenth(self, x, y):
        return y - x + 1
    """
    Quickly caculate all elements of nums does not exceed maxSum.
    """
    def getMinSum(self, n, index, index_value):
        maxMinusValue = index_value -1
        range_sum = (max(0, index - maxMinusValue), min(n-1, index + maxMinusValue))
        range_sum = self.rangeLenth(*range_sum)

        range_before_index = (max(0, index - maxMinusValue), index - 1)
        range_before_index = self.rangeLenth(*range_before_index)
        # Quick reference
        # [index]     index -1, index - 2, ..., index - index
        # [minusValue]       1,         2, ...,         index
        range_after_index = (index + 1, min(n-1, index + maxMinusValue))
        range_after_index = self.rangeLenth(*range_after_index)
        # Quick reference
        # [index]     index +1, index + 2, ..., index + n-1 - index
        # [minusValue]       1,         2, ...,         n-1 - index

        # All remain range isn't being cover have lowest posible value  = 1
        # Ass all number are postive (>0) 
        remainRange = n - range_sum
        baseBlock = index_value * range_sum + remainRange * 1

        # Breakout rule: we can only minus till 1, index_value-1 is the cap we can minus
        # So the range can't go down anymore is after index_value
        # range_before_index =   (index - (index_value -1), index - 1)
        # range_after_index =   (index + 1, index + (index_value -1))
        # range_sum = (index - (index_value -1), index + (index_value -1))

        
        # If we can't make it to the Breakout rule: minus is lower
        minusBeforeBlock = self.caculate1_n(range_before_index)
        minusAfterBlock = self.caculate1_n(range_after_index)
        
        minSum = baseBlock - minusBeforeBlock - minusAfterBlock
        return minSum
    
    """
    The sum of all the elements of nums does not exceed maxSum.
    """
    def quickCheck(self, n, index, index_value, maxSum):
        return self.getMinSum(n, index, index_value) <= maxSum
    
    def binarySearch(self, n, index, maxSum):
        left = 0
        right = maxSum*2


        for i in range(trunc(log(right-left, 2))+1):
            mid = (left + right) // 2
            if left == mid:
                break

            if self.quickCheck(n, index, mid, maxSum):
                left = mid
            else:
                right = mid
        # assert left == right -1, f"Logic error, can't search in log(n) time\n{left}, {right}"
        return left
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        return self.binarySearch(n, index, maxSum)


def test():
    a = Solution()

    testHelper = Test()
    testHelper.quickTest(a.getMinSum, (1, 0, 3), 3, "getMinSum 1")
    testHelper.quickTest(a.getMinSum, (2, 1, 3), 5, "getMinSum 2")
    testHelper.quickTest(a.getMinSum, (3, 1, 3), 7, "getMinSum 3")
    testHelper.quickTest(a.getMinSum, (3, 1, 1), 3, "getMinSum 4")
    testHelper.quickTest(a.getMinSum, (3, 1, 10), 28, "getMinSum 5")
    testHelper.quickTest(a.getMinSum, (8, 7, 3), 11, "getMinSum 6")
    testHelper.quickTest(a.getMinSum, (8, 7, 4), 14, "getMinSum 7")
    testHelper.quickTest(a.getMinSum, (8, 4, 5), 24, "getMinSum 8")
    testHelper.quickTest(a.getMinSum, (8, 4, 6), 32, "getMinSum 9")
    testHelper.quickTest(a.getMinSum, (8, 4, 7), 40, "getMinSum 10")
    testHelper.quickTest(a.getMinSum, (8, 4, 4), 17, "getMinSum 11")
    testHelper.quickTest(a.getMinSum, (8, 4, 3), 12, "getMinSum 12")
    testHelper.quickTest(a.maxValue, (4, 2, 6), 2, "Example 1")
    testHelper.quickTest(a.maxValue, (6, 1, 10), 3, "Example 2")
    testHelper.quickTest(a.maxValue, (8, 7, 14), 4, "Example 3")
    testHelper.quickTest(a.maxValue, (1321454, 7549, 132145444), 11832, "Example 4")
    testHelper.quickTest(a.maxValue, (13113, 43, 94914942), 13751, "Example 5")
    


if __name__ == "__main__":
    test()