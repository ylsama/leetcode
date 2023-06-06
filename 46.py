
"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List

"""
A full dfs problem, which each current state, we can caculate the adj state next to it

The last node will return full of the search order
"""
class Solution:
    def dfs(self, lastArray, adjNode):
        result = []

        if len(adjNode) == 0:
            result = lastArray
            return [result]
        
        for node in adjNode:
            newArray = lastArray + [node]
            newAdjNode = adjNode - set([node])
            result = result + self.dfs(newArray, newAdjNode)
        return result
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.dfs([], set(nums))


def test():
    a = Solution()
    # Example 1:
    nums = [1,2,3]
    result = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    print("Test 1 is", result == a.permute(nums))
    # Example 2:
    nums = [0,1]
    result = [[0,1],[1,0]]

    print("Test 2 is", result == a.permute(nums))
    # Example 3:
    nums = [1]
    result = [[1]]

    print("Test 3 is", result == a.permute(nums))

if __name__ == "__main__":
    test()