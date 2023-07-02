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

    """
    Second appoarch:
        A rearranged to form an arithmetic progression, is basically a sort process
        Here we try to find the diffent of each number:
            1. Find two lowest value number
                lowest_pos1 = min(arr, pos=0)
                lowest_pos2 = min(arr, pos=1)
            2. and caculate
                baseDifferences = lowest_pos2 - lowest_pos1
            This could be done using one search round O(n)
        After that, all the given value of the arithmetic progression array sould be calculated like this:
            item_index(i) == lowest_pos1 + baseDifferences*(i)

        We check if any item:
            1. isn't match this rule:
                    item_index(i) == lowest_pos1 + baseDifferences*(i)
            2. having value >  lowest_pos1 + baseDifferences*(len(arr)-1)
            3. is doubelicated
            then result is False
        else: return True

    """

    def canMakeArithmeticProgressionHardMode(self, arr: List[int]) -> bool:
        arr.sort()
        lastNumber = None
        # findMin
        lowest_pos1 = None
        lowest_pos2 = None
        for num in arr:
            if lowest_pos1 == None:
                lowest_pos1 = num
            elif lowest_pos1 > num:
                lowest_pos2 = lowest_pos1
                lowest_pos1 = num

        baseDifferences = lowest_pos2 - lowest_pos1
        isIndexFound = [False]*(len(arr))
        for num in arr:
            if (num - lowest_pos1) % baseDifferences == 0:
                return False
            if num > lowest_pos1 + baseDifferences*(len(arr)-1):
                return False
            if isIndexFound[(num - lowest_pos1) // baseDifferences)]
        return True


def test():
    a=Solution()
    # Example 1:
    arr=[3, 5, 1]
    result=True
    out=a.canMakeArithmeticProgression(arr)
    print("Test 1 is", result == out)
    # Example 2:
    arr=[3, 5, 1]
    result=True
    out=a.canMakeArithmeticProgression(arr)
    print("Test 2 is", result == out)
    # Example 3:_main__":
    arr=[randint(-10**6, 10**6) for i in range(1000)]
    out=a.canMakeArithmeticProgression(arr)
    print("Test time limit is OK")


if __name__ == "__main__":
    test()
