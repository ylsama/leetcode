"""
1091. Shortest Path in Binary Matrix

    Given an n x n binary matrix grid, return the length of the shortest
clear path in the matrix. If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell 
(i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected 
(i.e., they are different and they share an edge or a corner). The 
length of a clear path is the number of visited cells of this path.

"""
from typing import List


class Solution:
    def adjNode(self, x,y):
        result = []
        for i in range(-1,2):
            for j in range(-1,2):
                if not (i == j == 0) and (0 <= x+i < self.n and 0 <= y+j < self.n):
                    if self.grid[x+i][y+j] == 0:
                        result.append((x+i,y+j))
        return result
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.grid = grid
        trace = set()
        if grid[0][0] == 1:
            return -1
        
        queue = []
        queue.append(((1, 0,0)))
        while len(queue) > 0:
            step, x, y = queue.pop(0)
            if x == y == self.n -1:
                return step
            adjNode = self.adjNode(x, y)
            for x2,y2 in self.adjNode(x, y):
                if (x2,y2) in trace:
                    continue
                else:
                    trace.add((x2,y2))
                    queue.append((step+1, x2,y2))

        return -1

"""
Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 2

Example 2:
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1
 

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
"""
if __name__ == "__main__":
    a = Solution()
    result = a.shortestPathBinaryMatrix(grid = [[0,1],[1,0]])
    print("test 1 is", result == 2)
    result = a.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]])
    print("test 2 is", result == 4)
    result = a.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]])
    print("test 3 is", result == -1)
    result = a.shortestPathBinaryMatrix(grid = [[0 for i in range(100)] for i in range(100)])
    print("test time limit is ok")
        
