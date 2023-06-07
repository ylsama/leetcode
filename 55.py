"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
from random import randint
from typing import List

class Solution:
    """
    It seem go backward is easier, as you have more infomation required than jump forward blindly
    If you go backward, and found out you can't find a good standing point to jump to the position you standing at, it mean we could just stop and return False 
    
    We can skip some standing point if there is a better one that can jump our current end point.
    The code:

    1. We loop all the jumpEndPoint from the lastIndex = (n-1) to the beginnIndex = 0
    2. With each loop:
            Try to find a standingPoint where we can jump to our current jumpEndPoint
                which mean
                        Possible Jump Lengh >= Needed Jump Length

                    Where:
                        Needed Jump Length = jumpEndPoint - standingPoint
                        Possible Jump Lengh = nums[standingPoint]

            Every standingPoint that can't jump to our current jumpEndPoint can be skip,

            the next loop should start on founded standingPoint

    3. To end the loop: Ether we can't find standingPoint, or jumpEndPoint == beginIndex == 0
    """
    def canJump(self, nums: List[int]) -> bool:
        checkCanJump = True
        
        lastIndex = len(nums) - 1
        startingPoint = 0
        canBeSkip = [False]* len(nums)
        
        for jumpEndPoint in range(lastIndex, 0, -1):
            if jumpEndPoint == startingPoint:
                break

            if canBeSkip[jumpEndPoint]:
                continue
                
            neededJumpLength = 1
            
            standingPoint = jumpEndPoint
            
            for standingPoint in range(jumpEndPoint-1, -1, -1):
                if nums[standingPoint] >= neededJumpLength:
                    break
                neededJumpLength += 1
                canBeSkip[jumpEndPoint] = True
                
            if nums[standingPoint] < neededJumpLength:
                checkCanJump = False
                break
        
        return checkCanJump 
    
    
def test():
    a = Solution()
    # Example 1
    nums = [2,3,1,1,4]
    Output = True
    result = a.canJump(nums)
    print("Test 1 is", Output == result)
    # Example 2
    nums = [3,2,1,0,4]
    Output = False
    result = a.canJump(nums)
    print("Test 2 is", Output == result)
    # Example 3
    nums = [3]
    Output = True
    result = a.canJump(nums)
    print("Test 3 is", Output == result)
    # Example 4
    nums = [0]
    Output = True
    result = a.canJump(nums)
    print("Test 4 is", Output == result)
    # Example 5
    nums = [2,0]
    Output = True
    result = a.canJump(nums)
    print("Test 5 is", Output == result)
    # Constraints
    # 1 <= nums.length <= 10**4
    # 0 <= nums[i] <= 10**5
    nums = [randint(0,10**5) for i in range(10**4)]
    Output = True               # Pretty much
    result = a.canJump(nums)
    print("Test time limit is OK")

if __name__ == "__main__":
    test()
    
