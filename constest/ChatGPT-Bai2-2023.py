from random import randint

from national.testHelper import TestHelper

def getMax(array):
    max_value = float('-inf')
    for v in array:
        if v is not None and v > max_value:
            max_value = v
    return max_value

def getMin(array):
    min_value = float('inf')
    for v in array:
        if v is not None and v < min_value:
            min_value = v
    return min_value

def intersect(x, y, x2, y2):
    return x <= y2 and y >= x2

class MinMaxTree:
    def __init__(self, value, index, rangeLeft, rangeRight):
        self.value = value
        self.index = index
        self.rangeLeft = rangeLeft
        self.rangeRight = rangeRight
        self.max = value
        self.min = value
        self.left = None
        self.right = None

    def toDict(self):
        dictSelf = {
            "index": self.index,
            "value": self.value,
            "max": self.max,
            "min": self.min,
            "rangeLeft": self.rangeLeft,
            "rangeRight": self.rangeRight
        }
        if self.left:
            dictSelf["left"] = self.left.toDict()
        if self.right:
            dictSelf["right"] = self.right.toDict()
        return dictSelf

    def getMaxMin(self):
        if self.left:
            left_max, left_min = self.left.getMaxMin()
            self.max = max(self.max, left_max)
            self.min = min(self.min, left_min)
        
        if self.right:
            right_max, right_min = self.right.getMaxMin()
            self.max = max(self.max, right_max)
            self.min = min(self.min, right_min)
        
        return self.max, self.min

    def getMaxMinRange(self, queryLeft, queryRight):
        if not intersect(self.rangeLeft, self.rangeRight, queryLeft, queryRight):
            return None
        
        if self.max == self.min:
            return self.max, self.min
            
        result_max = []
        result_min = []

        if queryLeft <= self.index <= queryRight:
            result_max.append(self.value)
            result_min.append(self.value)

        if queryLeft <= self.rangeLeft <= self.rangeRight <= queryRight:
            result_max.append(self.max)
            result_min.append(self.min)

        if self.left and intersect(self.left.rangeLeft, self.left.rangeRight, queryLeft, queryRight):
            left_max, left_min = self.left.getMaxMinRange(queryLeft, queryRight)
            result_max.append(left_max)
            result_min.append(left_min)

        if self.right and intersect(self.right.rangeLeft, self.right.rangeRight, queryLeft, queryRight):
            right_max, right_min = self.right.getMaxMinRange(queryLeft, queryRight)
            result_max.append(right_max)
            result_min.append(right_min)
        
        return getMax(result_max), getMin(result_min)

    def update(self, value):
        if self.max < value:
            self.max = value
            self.min = value
            self.value = value
            return True
        
        is_updated = False

        if self.value < value:
            self.value = value
            is_updated = True

        if self.left and self.left.min < value:
            is_updated = self.left.update(value) or is_updated

        if self.right and self.right.min < value:
            is_updated = self.right.update(value) or is_updated 
        
        if is_updated:
            self.min = min(self.value, self.left.min if self.left else float('inf'), self.right.min if self.right else float('inf'))
        
        return is_updated

class MinMaxTreeFactory:
    def create(self, array, left, right):
        if left > right:
            return None
        
        index = left + (right - left) // 2
        value = array[index]
        root = MinMaxTree(value, index, left, right)
        root.left = self.create(array, left, index - 1)
        root.right = self.create(array, index + 1, right)
        root.getMaxMin()
        return root

class Solution:
    def solve(self, array, year, pairs):
        factory = MinMaxTreeFactory()
        min_max_tree = factory.create(array, 0, len(array) - 1)
        pairs = [(x - 1, y - 1) for x, y in pairs]  # TurnDownByOneIndex
        unchanged_year_start = 1

        for current_year, (l, r) in enumerate(pairs):
            max_value, _ = min_max_tree.getMaxMinRange(l, r)
            if min_max_tree.update(max_value):
                unchanged_year_start = current_year + 1
                # print(current_year+1, "change")

        return unchanged_year_start+1

def test():
    a = Solution()
    factoryTest = MinMaxTreeFactory()
    minMaxTree = factoryTest.create([7,8,9,10], 0, 3)
    test = TestHelper()
    array = [1232123,123,3,14,5,135,1,5616,4,57,48,7,6985,96,8906,0,1,7,8,9,10]
    minMaxTree = factoryTest.create(array, 0, len(array)-1)
    for r, l in [(0, 1), (1,3), (3,5), (1,9)]:
        test.quickTest(minMaxTree.getMaxMinRange, [r,l], (max(array[r:l+1]),min(array[r:l+1])))
    # print(factoryTest.create([8,3,3,4,7], 0, 4).toString())
    # print(factoryTest.create([9,5,8,4,8], 0, 4).toString())
    test.quickTest(a.solve, ([1,2,3,4], 4, [(2,2), (2,3), (1,2), (1,3)]), 3)
    array = [1232123,123,3,14,5,135,1,5616,4,57,48,7,6985,96,8906,0,1,7,8,9,10]
    pairs = [(2,2), (2,3), (2,4), (2,5), (2,8), (8,9), (8,13), (1,1), (1,5), (5,6), (6,15)]
    test.quickTest(a.solve, (array, len(pairs), pairs), 8)
    lenArray = 10**5
    randomWorstArray = [randint(-10**9, 10**9) for i in range(lenArray)]
    randomUpdatePair = []
    for i in range(lenArray):
        l = randint(1,lenArray)
        r = randint(l,min(l+160,lenArray))
        randomUpdatePair.append((l,r))
    test.quickTest(a.solve, (randomWorstArray, len(randomWorstArray), randomUpdatePair), 1)

if __name__ == "__main__":
    test()
