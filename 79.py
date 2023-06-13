from typing import List

from ulti.testHelper.testHelper import Test


class Solution:

    def findAdjNode(self, board, nodePosition, tracePath):
        rowID, columnID = nodePosition
        totalRow = len(board)
        totalColumn = len(board[0])
        adjReference = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        adjNodeArray = []

        for i, j in adjReference:
            adjRow = rowID + i
            adjColumn = columnID + j
            if (adjRow, adjColumn) in tracePath:
                continue
            if not (0 <= adjRow < totalRow and 0 <= adjColumn < totalColumn):
                continue
            adjNodeArray.append((rowID + i, columnID + j))

        return adjNodeArray

    def findPathToNextCharacter(self, board, position, tracePath, nextChar):
        result = []
        for nextPosition in self.findAdjNode(board, position, tracePath):
            row, column = nextPosition
            if board[row][column] != nextChar:
                continue
            nextTracePath = tracePath.copy()
            nextTracePath.add(nextPosition)
            result.append((nextPosition, nextTracePath))
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        # queue = [(adjNodeArray, traceSet)]
        queue = []
        totalRow = len(board)
        totalColumn = len(board[0])
        for row in range(totalRow):
            for column in range(totalColumn):
                if board[row][column] != word[0]:
                    continue
                position = (row, column)
                tracePath = set([position])
                queue.append((position, tracePath))
        if len(queue) == 0:
            return False

        while len(queue) > 0:
            position, tracePath = queue.pop()
            if len(tracePath) == len(word):
                return True
            char = word[len(tracePath)]
            foundPaths = self.findPathToNextCharacter(
                board, position, tracePath, char)
            for foundPath in foundPaths:
                queue.append(foundPath)
            if len(queue) == 0:
                return False

        return True


def main():
    a = Solution()
    board = [["A", "B", "C"]]
    test = Test()
    test.quickTest(a.exist, (board, "AB"), True)
    test.quickTest(a.exist, (board, "C"), True)
    test.quickTest(a.exist, (board, "BC"), True)
    test.quickTest(a.exist, (board, "CB"), True)
    test.quickTest(a.exist, (board, "BA"), True)
    test.quickTest(a.exist, (board, "D"), False)
    board = [["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"]]
    test.quickTest(a.exist, (board, "AAABBBCCC"), True)
    # board = [["A", "B", "C"]]*5000
    test.quickTest(a.exist, ([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
                   "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]], "AAAAAAAAAAAAAAB"), False)
    test.quickTest(a.exist, ([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
                   "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]], "AAAAAAAAAAAAAAa"), False)
    # test.quickTest(a.exist,(board,"A"*5000+"B"*5000+"C"*5000),True)


if __name__ == "__main__":
    main()
