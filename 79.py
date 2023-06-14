
from ulti.testHelper.testHelper import Test
from math import trunc, log
from typing import List


class Solution:
    def isPathConnected(self, path1, path2):
        path1LastElementIndex = len(path1) - 1
        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)

        row1, col1 = path1[path1LastElementIndex]
        row2, col2 = path2[0]
        relativedPossition = (row1 - row2, col1 - col2)
        if relativedPossition in [UP, RIGHT, LEFT, DOWN]:
            return True
        return False

    def isPathIntersec(self, path1, path2):
        if len(path1) == 0 or len(path2) == 0:
            return False
        isIntersec = False
        for cell in path1:
            if cell in path2:
                isIntersec = True
                break
        return isIntersec

    def findValidCombinedPath(self, str1FoundedPath, str2FoundedPath):
        validCombinedPath = []
        for str1Path in str1FoundedPath:
            for str2Path in str2FoundedPath:
                if not self.isPathConnected(str1Path, str2Path):
                    continue
                if self.isPathIntersec(str1Path, str2Path):
                    continue
                validCombinedPath.append(str1Path + str2Path)
        return validCombinedPath

    def findEachCharPath(self, board, charArray):
        foundedCharPath = {}
        isAllCharFound = True

        for rowID in range(len(board)):
            for columnID in range(len(board[0])):
                char = board[rowID][columnID]
                if char not in charArray:
                    continue
                if char not in foundedCharPath:
                    foundedCharPath[char] = []

                charPath = [(rowID, columnID)]
                foundedCharPath[char].append(charPath)

        for char in charArray:
            if char not in foundedCharPath:
                isAllCharFound = False
                break

        return foundedCharPath, isAllCharFound

    def splitToPairElement(self, array):
        remain = []
        pair = []
        if len(array) % 2 == 1:
            remain.append(array[len(array) - 1])

        for index in range(0, len(array) - len(remain), 2):
            pair.append(tuple(array[index:index+2]))

        return pair, remain

    def exist(self, board: List[List[str]], word: str) -> bool:
        N_TIME = len(word)
        LOG_N_TIME = trunc(log(N_TIME, 2)) + 1
        allFoundPath, isAllCharFound = self.findEachCharPath(board, word)
        if not isAllCharFound:
            return False

        splitedString = word
        for _ in range(LOG_N_TIME):
            pair, remain = self.splitToPairElement(splitedString)
            combinedStrings = []
            for str1, str2 in pair:
                newCombinedString = str1 + str2
                combinedStrings.append(newCombinedString)
                if newCombinedString in allFoundPath:
                    continue

                str1FoundedPath = allFoundPath[str1]
                str2FoundedPath = allFoundPath[str2]
                allFoundPath[newCombinedString] =\
                    self.findValidCombinedPath(str1FoundedPath, str2FoundedPath)
                
                if len(allFoundPath[newCombinedString]) == 0:
                    return False

            splitedString = combinedStrings
            if remain:
                splitedString += remain

        return True


def main():
    a = Solution()
    board = [["A", "B", "C"]]
    test = Test()
    test.quickTest(a.isPathConnected, ([(0, 1)], [(0, 2)]), True)
    test.quickTest(a.isPathConnected, ([(0, 1)], [(0, -2)]), False)
    test.quickTest(a.isPathConnected, ([(0, 1)], [(1, 2)]), False)
    test.quickTest(a.isPathConnected, ([(1, 1)], [(0, 2)]), False)
    test.quickTest(a.isPathConnected, ([(0, 1)], [(1, 0)]), False)
    test.quickTest(a.exist, (board, "AB"), True)
    test.quickTest(a.exist, (board, "C"), True)
    test.quickTest(a.exist, (board, "BC"), True)
    test.quickTest(a.exist, (board, "CB"), True)
    test.quickTest(a.exist, (board, "BA"), True)
    test.quickTest(a.exist, (board, "D"), False)
    board = [["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"]]
    test.quickTest(a.exist, (board, "AAABBBCCC"), True)
    test.quickTest(a.exist, ([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
        "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]], "AAAAAAAAAAAAAAB"), False)
    test.quickTest(a.exist, ([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
        "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]], "AAAAAAAAAAAAAAa"), False)
    test.quickTest(a.exist, ([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
        "A", "D", "E", "E"]], "ABCB"), False)
    test.quickTest(a.exist, ([["a", "a", "a", "a"], ["a", "a", "a", "a"], [
        "a", "a", "a", "a"]], "aaaaaaaaaaaaa"), False)
    board = [["A", "B", "C"]]*50
    test.quickTest(a.exist, (board, "A"*50+"B"*50+"C"*50), True)


if __name__ == "__main__":
    main()
