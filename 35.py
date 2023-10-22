from typing import List

class Solution:
    def searchInsert_easymode(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)  <= 50:
            return self.searchInsert_easymode(nums, target)
        n = len(nums)
        if nums[n-1] == target:
            return n-1
        elif nums[n-1] < target:
            return n
        elif nums[0] >= target:
            return 0
        l, r = 0, n
        while l+1<r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m
        return l
    
if __name__=="__main__":
    a = Solution()
    result = a.searchInsert(nums = [1,3,5,6], target = 5)
    print(result, result == 2)

    result = a.searchInsert(nums = [1,3,5,6], target = 0)
    print(result, result == 0)

    result = a.searchInsert(nums = [1,3,5,6], target = 7)
    print(result, result == 4)
