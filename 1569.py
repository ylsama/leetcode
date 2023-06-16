from typing import List

from ulti.testHelper.testHelper import TestHelper


class BinarySearchTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.totalNode = 1
        self.countWayCache = None
        if self.left != None:
            self.totalNode += self.left.totalNode
        if self.right != None:
            self.totalNode += self.right.totalNode

    def addNode(self, value):
        if self.value > value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.addNode(value)

        if self.value < value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.addNode(value)
        
        self.totalNode += 1

    def countWays(self, dp, modulo):
        if self.countWayCache != None:
            return self.countWayCache
        totalWay = 1
        if self.left == None and self.right == None:
            return totalWay
        if self.left == None:
            return self.right.countWays(dp, modulo)
        if self.right == None:
            return self.left.countWays(dp, modulo)
        
        totalWay = self.right.countWays(dp, modulo) * self.left.countWays(dp, modulo) * dp[self.left.totalNode][self.right.totalNode] % modulo
        self.countWayCache = totalWay
        return totalWay

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MODULO = 10**9 + 7
        root = None
        for n in nums:
            if root == None:
                root = BinarySearchTree(n)
            else:
                root.addNode(n)
        dp = [[0]*(len(nums) + 1) for i in range(len(nums) + 1)]

        for i in range(len(nums)+1):
            dp[i][0] = 1
            dp[0][i] = 1
        for i in range(1,len(nums)+1):
            for j in range(1,len(nums)+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MODULO

        totalWays = root.countWays(dp, MODULO)
        return totalWays - 1

def test():
    a = Solution()
    test = TestHelper()
    test.quickTest(a.numOfWays, [[2,1,3]], 1, "Example 1")
    test.quickTest(a.numOfWays, [[3,4,5,1,2]], 5, "Example 2")
    test.quickTest(a.numOfWays, [[1,2,3]], 0, "Example 3")

if __name__ == "__main__":
    test()