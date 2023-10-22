"""
1187. Make Array Strictly Increasing

Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.
"""
from ulti/testHelper/testHelper import TestHelper
from typing import List



class Solution:

    def inRange(self, value, rangeLeft, rangeRight):
        if value < rangeLeft:
            return -1
        if value > rangeRight:
            return 1
        return 0

    def findPossibleValue(self, arr2, rangeLeft, rangeRight, equad_is_greater = True):
        l = -1
        r = len(arr2)
        while True:
            m = (l+r) //2
            if l == m:
                break
            checkInRange = self.inRange(arr2(m), rangeLeft, rangeRight)
            if checkInRange == 0:
                if equad_is_greater:
                    r = m
                else:
                    l = m
                return True, arr2(m)
            if checkInRange > 0:
                r = m
            else:
                l = m
        return False, l
        
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(n + 1):
            for j in range(n + 1):




        for i in range():
        return 0

def test():
    test

if __name__=="__main__":
    test()
