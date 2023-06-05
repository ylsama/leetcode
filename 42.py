"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        traped_watter = 0
        watter_level = [10**5] * len(height)
        
        current_highest_wall = 0
        current_watter_level = 0
        
        for index in range(0,len(height)):
            wall = height[index] 
            if wall > current_highest_wall:
                current_highest_wall = wall
                current_watter_level = current_highest_wall
            watter_level[index] = min(watter_level[index] , current_watter_level)

        current_highest_wall = 0
        current_watter_level = 0
        for index in range(len(height)-1, -1, -1):
            wall = height[index] 
            if wall > current_highest_wall:
                current_highest_wall = wall
                current_watter_level = current_highest_wall
            watter_level[index] = min(watter_level[index] , current_watter_level)
        
        traped_watter = sum(watter_level) - sum(height)
        return traped_watter
    

    
def test():
    a = Solution()
    # Example 1:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = 6
    
    print("Test 1 is", a.trap(height) == result)
    
    # Example 2:
    height = [4,2,0,3,2,5]
    result = 9
    
    print("Test 2 is", a.trap(height) == result)

if __name__ == "__main__":
    test()