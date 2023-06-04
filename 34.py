"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from math import log, trunc
from typing import List

class Solution:
    """
    Binary search for the target, if target is found return the LeftMostIndex
    This can be achieved by setting search rule:
        nums[left] <  target <= nums[right]
    
    This mean, when the search is complete (left == mid == right-1)
        target <= nums[right] with right is minimal index
    
    We set and return "isFound" variable to be true if target == nums[right]
           and return leftMostIndex = right
    Because nums[left] = nums[right-1] < target
    """
    def binarySearchLeftMost(self, target): 
        leftMostIndex, isFound = -1, False
        
        left = -1
        right = len(self.nums)
        
        for i in range(self.MAX_LOG_N_LOOP):
            mid = (left + right) //2
            if left == mid:
                break
            
            if self.nums[mid] < target:
                left = mid
            else:
                right = mid
        
        if left + 1 == right:
            leftMostIndex = right
            if 0 <= right < len(self.nums):
                isFound = self.nums[right] == target
        else:
            raise "Logic fail, can't find in log(n) times"
        
        return leftMostIndex, isFound
        
    """
    Binary search for the target, if target is found return the rightMostIndex
    This can be achieved by setting search rule:
        nums[left] <=  target < nums[right]
    
    This mean, when the search is complete (left == mid == right-1)
        nums[left] <= target < nums[right] with right is minimal index
    
    We set and return "isFound" variable to be true if target == nums[left]
        rightMostIndex = left
    Because nums[left] = target < nums[right]
    """
    def binarySearchRightMost(self, target): 
        rightMostIndex, isFound = -1, False
        
        left = -1
        right = len(self.nums)
        
        for i in range(self.MAX_LOG_N_LOOP):
            mid = (left + right) //2
            if left == mid:
                break
            
            if self.nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if left + 1 == right:
            rightMostIndex = left
            if 0 <= left < len(self.nums):
                isFound = self.nums[left] == target
        else:
            raise "Logic fail, can't find in log(n) times"
        
        return rightMostIndex, isFound
        
    def searchRange(self, nums: List[int], target : int) -> List[int]:
        self.MAX_LOG_N_LOOP = trunc(log(len(nums)+2,2)) +1
        self.nums = nums
        self.target = target
        
        
        result = [-1, -1]
        
        leftMostIndex, isFound = self.binarySearchLeftMost(target)
        if isFound:
            result[0] = leftMostIndex
            
        rightMostIndex, isFound = self.binarySearchRightMost(target)
        if isFound:
            result[1] = rightMostIndex
        
        return result
    
def test():
    a = Solution()
    # Example 1:
    nums = [5,7,7,8,8,10]
    target = 8
    result = [3,4]
    print("Test 1 is", a.searchRange(nums, target) == result)
    # Example 2:
    nums = [5,7,7,8,8,10]
    target = 6
    result = [-1,-1]
    print("Test 2 is", a.searchRange(nums, target) == result)
    # Example 3:
    nums = []
    target = 0
    result = [-1,-1]
    print("Test 3 is", a.searchRange(nums, target) == result)
    
if __name__ == "__main__":
    test()