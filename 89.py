"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

"""
from random import randint
from typing import List

from ulti.testHelper.testHelper import TestHelper

class Solution:
    def getSortedIndexByHeight(self, heights):
        def sortKey(index):
            return heights[index]
        
        index = list(range(len(heights)))
        index.sort(key = sortKey, reverse = True)
        
        return index
    
    def findLargestRange(self, coveredRange):
        coveredRange.sort()
        maxRange = None
        currentRange = None
        for index in range(len(coveredRange)+1):
            if currentRange == None:
                currentRange = 1
            if 1 <= index < len(coveredRange):
                if coveredRange[index] == coveredRange[index - 1] + 1:
                    currentRange += 1
                    continue
            if maxRange == None:
                maxRange = currentRange
            if maxRange < currentRange:
                maxRange = currentRange
            currentRange = 1
        return maxRange


    def largestRectangleArea(self, heights: List[int]) -> int:
        sortedIndex = self.getSortedIndexByHeight(heights)
        coveredRange = [-1]*len(heights)
        maxRectangleArea = None
        currentHeight = None
        for heightsPointer in sortedIndex:
            if currentHeight == None:
                currentHeight = heights[heightsPointer]
            if currentHeight != heights[heightsPointer]:
                lagestRange = self.findLargestRange(coveredRange)
                if maxRectangleArea == None:
                    maxRectangleArea = currentHeight * lagestRange
                if maxRectangleArea < currentHeight * lagestRange:
                    maxRectangleArea = currentHeight * lagestRange
                    
            currentHeight = heights[heightsPointer]
            coveredRange.append(heightsPointer)
        
        return maxRectangleArea
        
def test():
    a = Solution()
    test = TestHelper()
    
    test.quickTest(a.getSortedIndexByHeight, [[1,2,3,4]], [3,2,1,0])
    test.quickTest(a.getSortedIndexByHeight, [[1,2,2,4]], [3,1,2,0])
    test.quickTest(a.getSortedIndexByHeight, [[4,2,3,4]], [0,3,2,1])
    test.quickTest(a.findLargestRange, [[1]], 1)
    test.quickTest(a.findLargestRange, [[1,2,3,4]], 4)
    test.quickTest(a.findLargestRange, [[4,2,3,1]], 4)
    test.quickTest(a.findLargestRange, [[5,6,3,1]], 2)
    test.quickTest(a.findLargestRange, [[15,1116,1233,1]], 1)
    # Example 1:
    heights = [2,1,5,6,2,3]
    result = 10
    test.quickTest(a.largestRectangleArea, [heights], result)
    # Example 2:
    heights = [2,4]
    result = 4
    test.quickTest(a.largestRectangleArea, [heights], result)
    test.quickTest(a.largestRectangleArea, [[15,1116,1233,1]], 2232)
    test.quickTest(a.largestRectangleArea, [[5,6,3,1]], 10)
    
    # Limit:
    heights = [randint(0,10**2) for i in range(10**5)]
    test.quickTest(a.largestRectangleArea, [heights], 1, "Limit time test")
    
if __name__ == "__main__":
    test()