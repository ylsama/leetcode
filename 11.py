"""
11. Container With Most Water

    - You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).
    - Find two lines that together with the x-axis form a container, such that the container contains the most water.
    - Return the maximum amount of water a container can store.
    - Notice that you may not slant the container. 

# Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
    the max area of water (blue section) the container can contain is 49.

# Example 2:
    Input: height = [1,1]
    Output: 1
 
# Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""


import random
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        # The problem could be slove with by go through each vertical lines
        # and find the best possible container that we could make using it
        #   1. max_containner = 0
        #   2. For each vertical lines: (vl_1)
        #           For each vertical lines:(vl_2)
        #               if (vl_1) != (vl_2) and max_containner < container_make(vl_1, vl_2):
        #                   max_containner = container_make(vl_1, vl_2) \
        #                               = min(vl_1, vl_2) * abs(index(vl_1) -  index(vl_2))
        # This could make faster
        #   1. We could go through (vl_1), (vl_2) only one time each
        #   2. When findding possible max_containner:
        #           2.1. We could make up a rule: the high of the container = vl_1 vertical lines
        #           2.2. Because, if there is better possible vl_2 < vl_1, we already find the
        #           max_containner[vl_2] already when loop through it
        #           2.3. Also, when this rule apply, the max_containner is only deppend on the length
        #           of index bettween two container.
        #           max_container = vl_1 * max[abs(index(vl_1) - index(vl_2) for each vl_2 > vl_1)]
        #
        # and the problem become find max
        #               abs(index(vl_1) - index(vl_2) for each vl_2 > vl_1)
        #
        # So, the first thing we could do is sort the provided vertical lines. which cost us O(n logn)
        # consider vl_2 > vl_1 already being sort. so we only need to loop every vl_2 element in the
        # left
        # We could turn this problem to find min max of index(vl_2) in provided array from [1..n],
        # [2..n], ... [i..n]...[n-1, n], which can be slove in O(n) time.
        #  abs(index(vl_1) - index(vl_2) = index(vl_1) - min(index(vl_2)) or index(vl_1) - max(index(vl_2))

        index_with_height = [(height[i], i) for i in range(n)]
        index_with_height.sort()

        max_containner = 0
        max_index = index_with_height[n-1][1]
        min_index = index_with_height[n-1][1]
        for i in range(n-2, -1, -1):
            vertical_line_1, current_vl_1_index = index_with_height[i]
            if max_containner < abs(max_index - current_vl_1_index) * vertical_line_1:
                max_containner = abs(
                    max_index - current_vl_1_index) * vertical_line_1
            if max_containner < abs(min_index - current_vl_1_index) * vertical_line_1:
                max_containner = abs(
                    min_index - current_vl_1_index) * vertical_line_1

            if max_index < current_vl_1_index:
                max_index = current_vl_1_index
            if min_index > current_vl_1_index:
                min_index = current_vl_1_index

        return max_containner


if __name__ == "__main__":
    a = Solution()
    result = a.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
    print("Test 1 is ", result == 49)
    result = a.maxArea(height=[1, 1])
    print("Test 2 is ", result == 1)
    result = a.maxArea(height=[random.randint(0, 10**4) for i in range(10**5)])
    print("Test time-limit is OK")
