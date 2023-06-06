"""
1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
"""
from random import randint
from typing import List


class Solution:
    """
    First appoarch (easy mode):
        A rearranged to form an arithmetic progression, is basically a sort process
        Here we using sort and check the diffent of each number to be equal
    """
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        lastNumber = None
        baseDifferences = arr[1] - arr[0]
        for num in arr:
            if lastNumber == None:
                lastNumber = num
                continue
            if num - lastNumber != baseDifferences:
                return False
            lastNumber = num
        return True
    
    
def test():
    a = Solution()
    # Example 1:
    arr = [3,5,1]
    result = True
    out = a.canMakeArithmeticProgression(arr)
    print("Test 1 is", result == out)
    # Example 2:
    arr = [3,5,1]
    result = True
    out = a.canMakeArithmeticProgression(arr)
    print("Test 2 is", result == out)
    # Example 3:_main__":
    arr = [randint(-10**6, 10**6) for i in range(1000)]
    out = a.canMakeArithmeticProgression(arr)
    print("Test time limit is OK")
    
    
# if __name__ == "__main__":
#     test() 