from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = list(zip(nums, cost))
        arr.sort()
        sumCost = [0] * len(arr)
        for i, (_, cost) in enumerate(arr):
            sumCost[i] += cost
            if i > 0:
                sumCost[i] += sumCost[i-1]

        def sumRange(sumCost, left, right):
            if left == -1:
                return sumCost[right]
            return sumCost[right] - sumCost[left]

        minNums = min(nums)
        res = [0] * len(arr)
        res[0] = sum([(num - minNums) * cost for num, cost in arr])

        for i in range(1, len(arr)):
            preNum, preCost = arr[i-1]
            num, cost = arr[i]
            res[i] = res[i - 1]
            res[i] += sumRange(sumCost, -1, i-1) * (-preNum + num)
            res[i] -= sumRange(sumCost, i-1, len(arr) - 1) * (num - preNum)

        return min(res)


def test():
    test = TestHelper()
    a = Solution()
    test.quickTest(a.minCost, [[1, 3, 5, 2], [2, 3, 1, 14]], 8)
    test.quickTest(a.minCost, [[2, 2, 2, 2, 2], [4, 2, 8, 1, 3]], 0)


if __name__ == "__main__":
    test()
