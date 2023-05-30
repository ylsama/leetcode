# 15. 3Sum

# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


import random
from typing import List


class Solution:
    # nums[i] range is lower than n so we can try to depend our code on this
    # because result triplet is not duplicate, so there could be some independent
    # on handling input
    # First appoard I will take is counting _ sort with dictionary hashtable
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums_dict = {}
        for i in nums:
            if not i in nums_dict: nums_dict[i] = 0
            nums_dict[i] += 1
        result = set()
        # I also using set, avoiding writing handling code to check the triplet is duplicate
        # This also mean the item need to hashable. so i will use Tupple
        #       1. The tupple in python is index dependent, so i will need to sort the triplet
        #       before adding to result_set
        # 
        # We loop through a.keys, which should alway < n
        for i in nums_dict.keys():
            for j in nums_dict.keys():
                # As j is on second loop, we not need to revisit i < j as we already done it
                # using previous loop
                # Also, if i==j, a[i] count need to be more than 2 so that we could use 2 number
                # if both of above condition is not meet, we can skip
                if (i == j and nums_dict[i] == 1) or i > j:
                    continue
                k = 0 -i -j
                if k in nums_dict:
                    # This is when i and j already checked, we only need to make sure the last
                    # number k is available in nums_array, which mean k in nums_dict
                    # But we will need to make sure to check if k == i == j or k ==j or k == i:
                    #   did we already use all available number in nums_array
                    #        if i == j == k then we need nums_dict[k] >= 3
                    #        if i != j, and i == k or j == k then we need nums_dict[k] >= 2
                    if nums_dict[k] < 2 and (k == i or k == j):
                        continue
                    if nums_dict[k] < 3 and (k == i == j):
                        continue

                    # The condition is meet, we have a tripplet, i just sort the tripplet and add
                    # it to the result set
                    if k < i:
                        result.add((k,i,j))
                    elif k < j:
                        result.add((i,k,j))
                    else:
                        result.add((i,j,k))
        # The problem want List[List(int)] so we need to change the type
        result = list(result)
        result = [list(i) for i in result]
        return result
        

if __name__ == "__main__":
    a = Solution()
    # Example 1:
    # Input: nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    Output = a.threeSum(nums = [-1,0,1,2,-1,-4])
    print("test 1 is", Output, Output == [[-1,-1,2],[-1,0,1]])
    #  Example 2:
    # Input: nums = [0,1,1]
    # Output: []
    Output = a.threeSum(nums = [0,1,1])
    print("test 2 is", Output, Output == [])
    # Example 3:
    # Input: nums = [0,0,0]
    # Output: [[0,0,0]]
    Output = a.threeSum(nums = [0,0,0])
    print("test 3 is", Output, Output == [[0,0,0]])
    # Constraints:
    # 3 <= nums.length <= 3000
    # -10**5 <= nums[i] <= 10**5
    Output = a.threeSum(nums = [-1,0,1,0])
    print("test 4 is", Output, Output == [[-1,0,1]])
    # Constraints:
    # 3 <= nums.length <= 3000
    # -10**5 <= nums[i] <= 10**5
    Output = a.threeSum(nums = [random.randint(-10**5,10**5) for i in range(3000)])
    print("test time limit is OK")

    

 
