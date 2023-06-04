"""
33. Search in Rotated Sorted Array


There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
from math import log, trunc
from random import randint
from typing import List




class Solution:
    """
    This return the shift point of the sorted array
    How? Reperesent the nums array as [1..n], the shift point is shiftPoint
         We have:
            - Sorted nums array: nums[1] < nums[2] < ... < nums[shiftPoint] < nums[shiftPoint+1] < .. < nums[n] 
            (as All values of nums are unique)
            - 0 <= shiftPoint < n

    The problem give us nums array being shifted 
            nums_index = [1            , 2           , .. n- shiftPoint,  ,..,    , n             ]
            nums_value = [shiftPoint +1, shiftPoint+2, .. n            , 1, 2, .. , (shiftPoint)  ]
    Then shift point is the only point where:
            - every element with nums_index <= n- shiftPoint have nums_value > nums_value[1]
            - every element with nums_index >  n- shiftPoint have nums_value < nums_value[1]
    
    We can use binary search to find n- shiftPoint:
        1. Start with pointerLeftIndex = 1, pointerRightIndex = n+1
                pointerLeftIndex = 1 <= n- shiftPoint
                pointerRightIndex= n+1 > n- shiftPoint

        2. Caculate the middle value:
                midIndex = (left + right)//2
                => left <= midIndex < right

        3. If nums_value[midIndex] > nums_value[1] then midIndex <= n- shiftPoint
                we can shift the pointerLeftIndex = midIndex
                else: we shift the pointerRightIndex = midIndex
        
        4. Repeat caculated midIndex value and shift pointerLeft/RightIndex until
                    pointerLeft == midIndex == (left + right)//2
                or:
                    pointerLeft  +1 == pointerRightIndex
        we now have:
                pointerLeftIndex  == midIndex <= n- shiftPoint
                pointerRightIndex == midIndex+1 > n- shiftPoint
                => pointerLeftIndex  == midIndex == n- shiftPoint
                => shiftPoint = n- pointerLeftIndex = n- midIndex
        5. return shiftPoint
    """
    def findShiftPoint(self):
        shiftPoint = -1
        isFound = False

        # Python index is from 0 .. n-1
        pointerLeftIndex = 0
        pointerRightIndex = len(self.nums)

        MAX_CAP_BINARY_SEARCH = trunc(log(len(self.nums), 2))+1
        for i in range(MAX_CAP_BINARY_SEARCH):
            midIndex = (pointerLeftIndex + pointerRightIndex) // 2
            if pointerLeftIndex == midIndex:
                break

            if  self.nums[midIndex] > self.nums[0]:
                pointerLeftIndex = midIndex
            else:
                pointerRightIndex = midIndex
        
        if pointerLeftIndex+1 == pointerRightIndex:
            shiftPoint = len(self.nums)-1 - pointerLeftIndex
            isFound = True
        else:
            raise "Logic error, can't find shiftPoint in log(n) time"
        return (shiftPoint, isFound)

    """
    After found the shift point, we can treat nums as two seperated sorted array
                     [startIndex                           endIndex]  
        nums_index = [1            , 2           , .. n- shiftPoint]
        nums_value = [shiftPoint +1, shiftPoint+2, .. n            ]
        
                     [startIndex                           endIndex]  
        nums_index = [n-shiftPoint+1, ..+2        , .. n           ]
        nums_value = [1             , 2           , .. shiftPoint  ]

    We can use normal binary search to find the target on each one
    """
    def binarySearch(self, startIndex,endIndex, target):
        targetIndex, isFound = -1, False
        left = startIndex-1
        right = endIndex +1

        MAX_CAP_BINARY_SEARCH = trunc(log(len(self.nums), 2))+1
        for i in range(MAX_CAP_BINARY_SEARCH):
            midIndex = (left + right) // 2
            if left == midIndex:
                break 

            if self.nums[midIndex] <= target:
                left = midIndex
            else:
                right = midIndex
        
        if left+1 == right:
            targetIndex = left
            if startIndex <= targetIndex <= endIndex:
                isFound = self.nums[targetIndex] == target
        else:
            raise "Logic error, can't find targetIndex in log(n) times"
        return (targetIndex, isFound)

    """
    Slove procedure:
    1. Find shift point of the provided array
    2. Using binarySearch to find the target in each sorted array
    3. If found the target, update result variable
    4. Return result 
    """
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        n = len(nums)
        result = -1

        shiftPoint, isFound = self.findShiftPoint()
        if not isFound:
            raise "can't find shift point, logic fail"
        
        targetIndex, isFound = self.binarySearch(0, n- shiftPoint -1, target)
        if isFound:
            result = targetIndex
        targetIndex, isFound = self.binarySearch(n- shiftPoint,n-1, target)
        if isFound:
            result = targetIndex

        return result
    
def main():
    a = Solution()
    # Example 1:
    # Input
    nums = [4,5,6,7,0,1,2]
    target = 0
    # Output 
    result = 4
    print ("Test 1 is", a.search(nums, target) == result)
    
    # Example 2:
    # Input: 
    nums = [4,5,6,7,0,1,2]
    target = 3
    # Output:
    result = -1
    print ("Test 2 is", a.search(nums, target) == result)

    # Example 3:
    # Input: 
    nums = [1]
    target = 0
    # Output: 
    result = -1
    print ("Test 3 is", a.search(nums, target) == result)

    # Constraints test:
    # 1 <= nums.length <= 5000
    # -10**4 <= nums[i] <= 10**4
    nums = [i for i in range(5000)]
    shift = randint(0, 4999)
    nums = nums[shift:] + nums[:shift]
    # All values of nums are unique.
    # nums is an ascending array that is possibly rotated.
    # -10**4 <= target <= 10**4
    target = 30
    result = (shift + target) % 5000
    print ("Test limit is OK", a.search(nums, target) == result)


    
if __name__ == "__main__":
    main()