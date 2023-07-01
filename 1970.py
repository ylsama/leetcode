from typing import List
from ulti.testHelper.testHelper import TestHelper


class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]


class Solution:
    def isValid(self, x, y, row, col):
        return 0 <= x < row and 0 <= y < col

    def getAdjCell(self, x, y, row, col):
        UP_RIGHT_DOWN_LEFT = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        DIAGNAL = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        arr = []
        for changeRow, chaneCol in UP_RIGHT_DOWN_LEFT + DIAGNAL:
            modifiedX, modifiedY = x + changeRow, y + chaneCol
            if self.isValid(modifiedX, modifiedY, row, col):
                arr.append((modifiedX, modifiedY))

        return arr

    def latestDayToCross(self,
                         row: int,
                         col: int,
                         cells: List[List[int]]) -> int:
        cells = [[x-1, y-1] for x, y in cells]
        dsu = DSU(row * col + 2)
        grid = [[0] * col for _ in range(row)]

        for index, (r, c) in enumerate(cells):
            grid[r][c] = 1
            dsu_index = r * col + c + 1
            for new_r, new_c in self.getAdjCell(r, c, row, col):
                index_new = new_r * col + new_c + 1
                if grid[new_r][new_c] == 1:
                    dsu.union(dsu_index, index_new)

            if c == 0:
                dsu.union(0, dsu_index)
            if c == col - 1:
                dsu.union(row * col + 1, dsu_index)
            if dsu.find(0) == dsu.find(row * col + 1):
                result = index
                return result


def test():
    test = TestHelper()
    a = Solution()
    test.fileTest(a.latestDayToCross,
                  testFileInput=r"test/1970/1.inp",
                  testFileOutput=r"test/1970/1.out")
    test.fileTest(a.latestDayToCross,
                  testFileInput=r"test/1970/2.inp",
                  testFileOutput=r"test/1970/2.out")
    test.fileTest(a.latestDayToCross,
                  testFileInput=r"test/1970/3.inp",
                  testFileOutput=r"test/1970/3.out")


if __name__ == "__main__":
    test()
