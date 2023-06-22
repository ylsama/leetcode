"""
714. Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on
the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions
as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).
"""
from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def maxProfitLowSpace(self, prices: List[int], fee: int) -> int:
        bestProfit = [0, 0]
        for step, price in enumerate(prices):
            if step == 0:
                bestProfit[1] = - prices[0]
                continue

            currentBestProfit = [0, 0]
            currentBestProfit[1] = max(bestProfit[1], bestProfit[0] - price)
            currentBestProfit[0] = max(
                bestProfit[0], bestProfit[1] + price - fee)
            bestProfit = currentBestProfit
        return bestProfit[0]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        bestProfit = [[0, 0] for i in range(n+1)]
        for step, price in enumerate(prices):
            if step == 0:
                bestProfit[1][1] = - prices[0]
                continue

            possibleCase = []
            possibleCase.append(bestProfit[step][1])
            possibleCase.append(bestProfit[step][0] - price)
            bestProfit[step+1][1] = max(possibleCase)

            possibleCase = []
            possibleCase.append(bestProfit[step][0])
            possibleCase.append(bestProfit[step][1] + price - fee)
            bestProfit[step+1][0] = max(possibleCase)
        return bestProfit[n][0]


def test():
    test = TestHelper()
    a = Solution()

    test.quickTest(a.maxProfit, [[1], 0], 0)
    test.quickTest(a.maxProfit, [[1], 0], 0)
    test.quickTest(a.maxProfit, [[1, 2], 3], 0)
    test.quickTest(a.maxProfit, [[1, 2], 0], 1)
    test.quickTest(a.maxProfitLowSpace, [[4, 2], 0], 0)
    test.quickTest(a.maxProfitLowSpace, [[1, 2], 3], 0)
    test.quickTest(a.maxProfitLowSpace, [[1, 2], 0], 1)
    test.quickTest(a.maxProfitLowSpace, [[4, 2], 0], 0)


if __name__ == "__main__":
    test()
