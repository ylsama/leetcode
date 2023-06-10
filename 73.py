# """
# 73. Set Matrix Zeroes
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
# Could you devise a constant time solution?
# - This just not practical, as inputing a m x n table will cost you m x n time already
# - They do right about O(mn) which not chalenging
#
# - A O(m+n) mean we only need to one round loop to find all Zero
# Which is weird? And only happend when
# Let say, all Zero is on one round and one column
#
# Also, changing all other block to Zero require one more loop. Which if the table provided is all Zero in it's diagonal, you will need to set all other m*n to Zero
# So even the best way still need m * n time to change Matrix to Zero
#
# So we can only have a O(mn) time solution, Space is different story
# - Using 2 Recorded table to store  row and column could work as O(m+n) space
# - Using the matrix it self could do it too, just asumming that first row and Column is our recorded table
# """
from typing import List


class Solution:
    def setRecordRowZero(self, matrix, index):
        FIRST_COLUMN_ID = 0
        matrix[index][FIRST_COLUMN_ID] = 0

    def checkRecordRowZero(self, matrix, index):
        FIRST_COLUMN_ID = 0
        return matrix[index][FIRST_COLUMN_ID] == 0

    def setRecordColumnZero(self, matrix, index):
        FIRST_ROW_ID = 0
        matrix[FIRST_ROW_ID][index] = 0

    def checkRecordColumnZero(self, matrix, index):
        FIRST_ROW_ID = 0
        return matrix[FIRST_ROW_ID][index] == 0

    def setRowZero(self, matrix, rowID):
        for currentColumn in range(len(matrix[rowID])):
            matrix[rowID][currentColumn] = 0

    def setColumnZero(self, matrix, columnID):
        for currentRow in range(len(matrix)):
            matrix[currentRow][columnID] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # """
        # Do not return anything, modify matrix in-place instead.
        # """
        totalRows = len(matrix)
        totalColumn = len(matrix[0])

        FIRST_ROW_ID = 0
        FIRST_COLUMN_ID = 0

        firstRowZero = False
        firstColumnZero = False
        # """
        # Here we check firstRow and firstColumn before trying to modify and using them as our recorded table
        # """
        for currentColumn in range(totalColumn):
            if matrix[FIRST_ROW_ID][currentColumn] == 0:
                firstRowZero = True
                break

        for currentRow in range(totalRows):
            if matrix[currentRow][FIRST_COLUMN_ID] == 0:
                firstColumnZero = True
                break
        # """
        # We create a setRecord function each on Row and Column, to set and use the first row/column of the matrix to be our recorded table
        # """
        for currentRow in range(totalRows):
            for currentColumn in range(totalColumn):
                if matrix[currentRow][currentColumn] == 0:
                    self.setRecordRowZero(matrix, currentRow)
                    self.setRecordColumnZero(matrix, currentColumn)

        # """
        # After that, our matrix is update, here i checking with each Row, if it is recorded to be a Zero row, we update it all to 0;
        # I specificly skip the first row, as it being use as our recorded infomation array
        # """
        for currentRow in range(1, totalRows):
            if self.checkRecordRowZero(matrix, currentRow):
                self.setRowZero(matrix, currentRow)

        # """
        # The same with our Column
        # """
        for currentColumn in range(1, totalColumn):
            if self.checkRecordColumnZero(matrix, currentColumn):
                self.setColumnZero(matrix, currentColumn)

        # """
        # In case of which we need to set our first row or column to Zero
        # Meanning there is Zero in our first Row or Column, we sould have check and safe the infomation before hand
        # """
        if firstRowZero:
            self.setRowZero(matrix, 0)

        if firstColumnZero:
            self.setColumnZero(matrix, 0)
