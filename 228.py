from typing import List


class Solution:
    def toRange(self, left, right):
        if left == right:
            return f"{left}"
        return f"{left}->{right}"
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        currentRange = None
        rangeList = []
        for i in range(len(nums)+1):
            if currentRange == None:
                currentRange = [i,i]
                continue
            if i >= len(nums):
                rangeList.append(self.toRange(*[nums[i] for i in currentRange]))
                break
            if nums[i] == nums[i-1] + 1:
                currentRange[1] = i
            else:
                rangeList.append(self.toRange(*[nums[i] for i in currentRange]))
                currentRange = [i,i]
                
        return rangeList