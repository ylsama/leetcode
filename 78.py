"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Recruition call shuld be evil, and you will never want to use it

Here we setup a simple approad
    1. If we already have the result of
            subsets(nums[1..n-1])

    and want to add another element nums[n]
    2. All subsets(nums[1..n-1]) need to be in the final_result
    3. Newly created sub set will contain the nums[n]
    As all the numbers of nums are unique.

        3.1. We add nums[n] to all sub_set in subsets(nums[1..n-1])
        3.2. Add all newly created sub_set in to final_result

    4. Return final_result

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        lastElement = nums.pop()
        otherToSubSets = self.subsets(nums)
        subSets = []
        for e in [[], [lastElement]]:
            for o in otherToSubSets:
                subSets.append(o + e)
        return subSets


def test():
    a = Solution()
    nums = [1, 2, 3]
    out = a.subsets(nums)
    result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print("Test 1 is", out == result)

    nums = [0]
    out = a.subsets(nums)
    result = [[], [0]]
    print("Test 2 is", out == result)


if __name__ == "__main__":
    test()
