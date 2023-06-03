"""
2101. Detonate the Maximum Bombs
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and 
yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the 
radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie 
in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
"""

from random import randint
from typing import List
from math import sqrt

# A simple dfs search, graph problem to find the biggest group of Node that
# each Node can go to any other Node in the group 
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        nodeAdjTable = {}
        result = 0
        
        def getEulerRangeSquare(x,y, x2, y2):
            return (x - x2)** 2 + (y - y2)**2
        
        def adjCheck(bomb1, bomb2):
            result = False
            x,y, r1 = tuple(bomb1)
            x2,y2, r2 = tuple(bomb2)
            eulerRange = getEulerRangeSquare(x,y , x2,y2)
            if eulerRange <= r1  ** 2:
                result = True
            return result

        def dfs(node):
            result = 1
            if not node in nodeAdjTable:
                return result
            
            for adjNode in nodeAdjTable[node]:
                if trace[adjNode]:
                    trace[adjNode] = False
                    result += dfs(adjNode)
            return result

        # edgeTable = {}
        for index_bomb1 in range(len(bombs)):
            for index_bomb2 in range(len(bombs)):
                if index_bomb1 == index_bomb2:
                    continue
                bomb1 = bombs[index_bomb1]
                bomb2 = bombs[index_bomb2]
                if adjCheck(bomb1, bomb2):
                    if not index_bomb1 in nodeAdjTable:
                        nodeAdjTable[index_bomb1] = []
                    nodeAdjTable[index_bomb1].append(index_bomb2)

        for index in range(len(bombs)):
            trace = [True for i in bombs]
            if trace[index]:
                trace[index] = False
                totalDenotedBombs = dfs(index)
                if result < totalDenotedBombs:
                    result = totalDenotedBombs
        return result


if __name__ == "__main__":
    a = Solution()
    # Example 1:
    # Input: bombs = [[2,1,3],[6,1,4]]
    # Output: 2
    # Explanation:
    # The above figure shows the positions and ranges of the 2 bombs.
    # If we detonate the left bomb, the right bomb will not be affected.
    # But if we detonate the right bomb, both bombs will be detonated.
    # So the maximum bombs that can be detonated is max(1, 2) = 2.
    result = a.maximumDetonation(bombs = [[2,1,3],[6,1,4]])
    print("Test 1 is", result == 2)

    # Example 2:
    # Input: bombs = [[1,1,5],[10,10,5]]
    # Output: 1
    # Explanation:
    # Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
    result = a.maximumDetonation(bombs = [[1,1,5],[10,10,5]])
    print("Test 2 is", result == 1)

    # Example 3:
    # Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    # Output: 5
    # Explanation:
    # The best bomb to detonate is bomb 0 because:
    # - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
    # - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
    # - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
    # Thus all 5 bombs are detonated.
    result = a.maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])
    print("Test 3 is", result == 5)

    result = a.maximumDetonation(bombs = [[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]])
    print("Test 4 is", result == 1)
    
    result = a.maximumDetonation(bombs = [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]])
    print("Test 5 is", result == 9)

    # Constrain
    # 1 <= bombs.length <= 100
    # bombs[i].length == 3
    # 1 <= xi, yi, ri <= 105
    result = a.maximumDetonation(bombs = [[randint(1, 105), randint(1, 105), randint(1, 105)] for i in range(100)])
    print("Test time-limit is ok")
