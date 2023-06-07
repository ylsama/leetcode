"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.


"""

from typing import List


class Solution:
    """
    We could easily find the maxSum using this strategy:
        1. Caculate sumNums = [sum(nums[:i]) for i in range(1..n)] 
        2. Find minSums[i] = [min(sumNums[:i]) for i in range(1..n)]
        3. maxSum = max([sumNums[i] - minSums[i] for i in range(1..n)])
        
    How?
        1. Let call our wanted to find subarray being represent as (left, right)
                sum of subarray(left, right)  =  sum(num[:right]) - sum(num[:left]) 
                
        -> to quickly caculate sum of subarray, we can pre-caculated sum table in O(n) time
        
        2. Here, asumming right position is unchange, to maximize sum of subarray 
        we need to find the minimize sum(num[:left])
                Which mean:
                    finding the min(sum of subarray[0..right])
                with every "right" position
        
        -> to quickly caculate min of subarray, we can pre-caculated min table in O(n) time
        
        3. After that, loop trough every "right" position,
                try to caculate the best possible sum of subarray
                
        -> the maximum sum of subarray will be the required result 
    """
    def maxSubArray(self, nums: List[int]) -> int:
        sumNums = [0]*(len(nums)+1)
        for i in range(1, len(nums) +1):
            sumNums[i] = sumNums[i-1] + nums[i-1]
            
        minSums = [0]*(len(nums)+1)
        for i in range(1, len(nums) +1):
            minSums[i] = sumNums[i]
            if minSums[i] > minSums[i-1]:
                minSums[i] = minSums[i-1]
        
        maxSum = None
        for right in range(1, len(nums) +1):
            currentMaxSum =  sumNums[right] - minSums[right-1]
            if maxSum == None:
                maxSum = currentMaxSum
            if maxSum < currentMaxSum:
                maxSum = currentMaxSum
        
        return maxSum
        
        
def test():
    a = Solution()
    # Example 1:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output = 6
    result = a.maxSubArray(nums)
    print("Test 1 is", Output == result)
    # Example 2:
    nums = [1]
    Output = 1
    result = a.maxSubArray(nums)
    print("Test 2 is", Output == result)
    # Example 3:
    nums = [5,4,-1,7,8]
    Output = 23
    result = a.maxSubArray(nums)
    print("Test 3 is", Output == result)
    # Example 4:
    nums = [-1]
    Output = -1
    result = a.maxSubArray(nums)
    print("Test 4 is", Output == result)
    
if __name__ == "__main__":
    test()