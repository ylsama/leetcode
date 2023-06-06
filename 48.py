"""
48. Rotate Image


You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


"""
Rotation 90*

[1,2,3,4,5]
[6,7,8,9,10]
...

This just mean try turn column into row (normally) 
"""
from typing import List

"""
There is some thing to said about python variable

Every pass param to a python function is a referen, where any change to variable mean it will change, persistence after the "callback"
    This is not like the C/C++ in which
        1. The default variable param will be value passing only, meaning more alocating and the changing will not persist
        2. Unless you use specific &var , which mean the function is specific you to send the reference
"""
class Solution:
    def rotate_sane(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        tempMatrix = []
        for columnID in range(n):
            tempColumn = []
            for rowID in range(n-1,-1,-1):
                tempColumn.append(matrix[rowID][columnID])
                
            tempMatrix.append(tempColumn)
            
        for rowID in range(n):
            for columnID in range(n):
                matrix[rowID][columnID] = tempMatrix[rowID][columnID]
        return tempMatrix
    
    """
        swap top to bottom, rather say easy
    """
    def upSideDown(self, matrix):
        n = len(matrix)
        
        for rowID in range(n//2):
            for columnID in range(n):
                tmp = matrix[n-1 - rowID][columnID]
                matrix[n-1 - rowID][columnID] = matrix[rowID][columnID]
                matrix[rowID][columnID] = tmp
        print("Updown", matrix, sep='\n')
    
    """
        swap TopLeft to BottomRight, which just mean column in to row and row to column
    """
    def diagonalTopLeftBottomRight(self, matrix):
        n = len(matrix)
        
        for rowID in range(n):
            for columnID in range(rowID +1, n):
                tmp = matrix[columnID][rowID]
                matrix[columnID][rowID] = matrix[rowID][columnID]
                matrix[rowID][columnID] = tmp
        print("diagonalTopLeftBottomRight", matrix, sep='\n')

    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.upSideDown(matrix)
        self.diagonalTopLeftBottomRight(matrix)


def test():
    a = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output = [[7,4,1],[8,5,2],[9,6,3]]
    a.rotate(matrix)
    print('Test 1 is', Output == matrix)
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    a.rotate(matrix)
    print('Test 2 is', Output == matrix)

if __name__ == "__main__":
    test()