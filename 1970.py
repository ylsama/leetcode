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


class ForestNode:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.size = 1
        self.rank = 0

    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()
            return self.parent
        else:
            return self
    
    def toString(self):
        x = self
        arr = []
        while x.parent != x:
            arr.append(x.parent.id)
            x = x.parent
        return arr
    
    def findConstantMemory(self):
        root = self
        while root.parent != root:
            root = root.parent

        x = self
        while x.parent != root:
            parent = x.parent
            x.parent = root
            x = parent

        return root
    
    def findWithPathSplitting(self):
        x = self
        while x.parent != x:
            x, x.parent = x.parent, x.parent.parent
        return x
    
    def findWithPathHalving(self):
        x = self
        while x.parent != x:
            x.parent = x.parent.parent
            x = x.parent
        return x
    
    def union(self, newForestNode):
        x = self.find()
        y = newForestNode.find()
        if x == y:
            return
    
        if x.size < y.size:
            x, y = y, x

        y.parent = x
        x.size = x.size + y.size
    
    def unionByRank(self, newForestNode):
        x = self.find()
        y = newForestNode.find()
        if x == y:
            return
    
        if x.rank < y.rank:
            x, y = y, x

        y.parent = x
        if x.rank == y.rank:
            x.rank = x.rank + 1
            
class disjointSetForest:
    def __init__(self, ):
        self.forest = {}

    def makeSet(self, x):
        if x not in self.forest:
            self.forest[x] =  ForestNode(x)

    def union(self, x, y):
        self.forest[x].union(self.forest[y])

    def find(self, x):
        return self.forest[x].find()
        
    def getAllNodeRoot(self):
        return [self.forest[x].find().id for x in self.forest]
    
    def toString(self):
        dict = {}
        for x in self.forest:
            dict[x] = self.forest[x].toString()
        return dict

class Solution:
    def isValid(self, x, y, row, col):
        return 0 <= x < row and 0 <= y < col

    def adjCell(self, x, y, row, col):
        UP_RIGHT_DOWN_LEFT = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        DIAGONAL = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        for changeRow, chaneCol in UP_RIGHT_DOWN_LEFT + DIAGONAL:
            modifiedX, modifiedY = x + changeRow, y + chaneCol
            if self.isValid(modifiedX, modifiedY, row, col):
                yield (modifiedX, modifiedY)

    def latestDayToCross(self,
                         row: int,
                         col: int,
                         cells: List[List[int]]) -> int:
        cells = [[x-1, y-1] for x, y in cells]

        dsu = disjointSetForest()
        dsu.makeSet("left")
        dsu.makeSet("right")
        for row_id in range(row):
            for col_id in range(col):
                dsu.makeSet((row_id, col_id))

        grid = [[0] * col for _ in range(row)]

        for index, (r, c) in enumerate(cells):
            grid[r][c] = 1
            for new_r, new_c in self.adjCell(r, c, row, col):
                if grid[new_r][new_c] == 1:
                    dsu.union((r, c), (new_r, new_c))

            if c == 0:
                dsu.union("left", (r, c))
            if c == col - 1:
                dsu.union("right", (r, c))

            if dsu.find("left") == dsu.find("right"):
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
