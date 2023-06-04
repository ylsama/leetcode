"""
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List


class Solution:
    """
    Get all the row of the board and return as a array

    The input board infomation is already in form of row array
    """
    def getRows(self) -> List[List[str]]:
        rows = []
        for rowIndex in range(9):
            rows.append(self.board[rowIndex])
        return rows

    """
    Get all the column of the board and return as a array

    The column is where we want to get:
        1. Let say we want to get column with column_index provided
                column = []

        2. We have the board is present in this form 
                (row_index, column_index) --> board[row_index][column_index]
        So element in that column_index will be
                for row_index in [1..9]:
                    columns[column_index].append(board[row_index][column_index])
    """
    def getColumn(self, columnIndex) -> List[str]:
        column = []
        for rowIndex in range(9):
            column.append(self.board[rowIndex][columnIndex])
        return column

    """
    Get all the column of the board and return as a array
    """
    def getColumns(self) -> List[List[str]]:
        columns = []
        for columnIndex in range(9):
            column = self.getColumn(columnIndex)
            columns.append(column)
        return columns
        
    """
    Get all the subBox of the board and return as a array

    The subBox is a 3x3 box:
        1. Let say we want to get a subBox with subBoxIndex = top-left point = x, y
                subBox = []
        We know that element in that subBox will be:
            collumn_index:  y          y+1          y+2 
            row_index:               
            x              [(x  ,y)    (x  ,y+1)    (x  ,y+2)]
            x+1            [(x+1,y)    (x+1,y+1)    (x+1,y+2)]
            x+2            [(x+2,y)    (x+2,y+1)    (x+2,y+2)]

        2. We have the board is present in this form 
                (row_index, column_index) --> board[row_index][column_index]
        So to get all the element, we just need to do 2 for loop and append the element in to subBox
                for row_index in [x..x+3]:
                    for row_index in [x..x+3]:
                        subBox.append(board[row_index][column_index])
    """
    def getSubBox(self,subBoxIndex) -> List[str]:
        subBox = []
        x, y = subBoxIndex
        for i in range(x,x+3):
            for j in range(y,y+3):
                subBox.append(self.board[i][j])
        return subBox
    
    """
    Get all the subBox of the board and return as a array
    """
    def getSubBoxes(self) -> List[List[str]]:
        subBoxes = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                subBox = self.getSubBox((i,j))
                subBoxes.append(subBox)
        return subBoxes
    
    """
    Check if is there any number were repeat
    1. Loop through provided array
    2. We append found, not repeated number into a hash set
    3. If a repeated number is found,
            return True
    4. If we already loop through all available array
            return False
        which mean there is no repeated number found in array
    """
    def checkDigitsRepetitionInvalid(self, array) -> bool:
        result = False
        
        numberFound = set()
        for num in array:
            if num == '.':
                continue
            if num in numberFound:
                return True
            else:
                numberFound.add(num)
        return result
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        result = True
        
        rows = self.getRows()
        columns = self.getColumns()
        subBoxes = self.getSubBoxes()
        # Rule check
        
        # Each row must contain the digits 1-9 without repetition.
        for row in rows:
            isInvalid = self.checkDigitsRepetitionInvalid(row)
            if isInvalid:
                return False

        # Each column must contain the digits 1-9 without repetition.
        for column in columns:
            isInvalid = self.checkDigitsRepetitionInvalid(column)
            if isInvalid:
                return False
            
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for subBoxe in subBoxes:
            isInvalid = self.checkDigitsRepetitionInvalid(subBoxe)
            if isInvalid:
                return False
        return result
    
def test():
    a = Solution()
    # Example 1:
    board = \
            [["5","3",".",".","7",".",".",".","."] \
            ,["6",".",".","1","9","5",".",".","."] \
            ,[".","9","8",".",".",".",".","6","."] \
            ,["8",".",".",".","6",".",".",".","3"] \
            ,["4",".",".","8",".","3",".",".","1"] \
            ,["7",".",".",".","2",".",".",".","6"] \
            ,[".","6",".",".",".",".","2","8","."] \
            ,[".",".",".","4","1","9",".",".","5"] \
            ,[".",".",".",".","8",".",".","7","9"]]
    result = True
    print("Test 1 is", result == a.isValidSudoku(board))
    # Example 2:
    board = \
            [["8","3",".",".","7",".",".",".","."] \
            ,["6",".",".","1","9","5",".",".","."] \
            ,[".","9","8",".",".",".",".","6","."] \
            ,["8",".",".",".","6",".",".",".","3"] \
            ,["4",".",".","8",".","3",".",".","1"] \
            ,["7",".",".",".","2",".",".",".","6"] \
            ,[".","6",".",".",".",".","2","8","."] \
            ,[".",".",".","4","1","9",".",".","5"] \
            ,[".",".",".",".","8",".",".","7","9"]]
    result = False
    print("Test 2 is", result == a.isValidSudoku(board))
    # Example 3:
    board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    result = False
    print("Test 3 is", result == a.isValidSudoku(board))

if __name__=="__main__":
    test()
    