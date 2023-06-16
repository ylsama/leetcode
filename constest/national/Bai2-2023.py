import json
from random import randint

from testHelper import TestHelper

def getMax(array):
    max = None
    for v in array:
        if v == None:
            continue
        if max == None:
            max = v 
        if max < v:
            max = v
    return max

def getMin(array):
    min = None
    for v in array:
        if v == None:
            continue
        if min == None:
            min = v 
        if min > v:
            min = v
    return min

def interset(x,y, x2, y2):
    case1 =  x <= x2 <= y 
    case2 =  x2 <= x <= y2 
    return case1 or case2

class MinMaxTree:
    def __init__(self, value, index, rangeLeft, rangeRight):
        self.value = value
        self.index = index
        self.rangeLeft = rangeLeft
        self.rangeRight = rangeRight
        self.max = None
        self.min = None
        self.left = None
        self.right = None

    def toDict(self):
        dictSelf = {}
        dictSelf["index"] = self.index
        dictSelf["value"] = self.value
        dictSelf["max"] = self.max
        dictSelf["min"] = self.min
        dictSelf["rangeLeft"] = self.rangeLeft
        dictSelf["rangeRight"] = self.rangeRight
        if self.left:
            dictSelf["left"] = self.left.toDict()
        if self.right:
            dictSelf["right"] = self.right.toDict()
        return dictSelf

    def getMaxMin(self):
        if self.max != None and self.min != None:
            return (self.max, self.min)
        
        if self.max == None:
            self.max = self.value
        if self.min == None:
            self.min = self.value
        
        if self.left != None:
            leftMax, leftMin = self.left.getMaxMin()
            if self.max < leftMax:
                self.max = leftMax
            if self.min > leftMin:
                self.min = leftMin
        if self.right != None:
            rightMax, rightMin = self.right.getMaxMin()
            if self.max < rightMax:
                self.max = rightMax
            if self.min > rightMin:
                self.min = rightMin

        return (self.max, self.min)

    def getMaxMinRange(self, queryLeft, queryRight):
        if not interset(self.rangeLeft, self.rangeRight, queryLeft, queryRight):
            return None
        if self.max == self.min:
            return self.max, self.min
            
        resultMax = []
        resultMin = []
        if queryLeft <= self.index <= queryRight:
            resultMax.append(self.value)
            resultMin.append(self.value)
        if queryLeft <= self.rangeLeft <= self.rangeRight <= queryRight:
            resultMax.append(self.max)
            resultMin.append(self.min)
        
        if self.left != None:
            x1, y1 = self.left.rangeLeft, self.left.rangeRight
            if interset(x1, y1, queryLeft, queryRight):
                leftMax, leftMin = self.left.getMaxMinRange(queryLeft, queryRight)
                resultMax.append(leftMax)
                resultMin.append(leftMin)

        if self.right != None:
            x1, y1 = self.right.rangeLeft, self.right.rangeRight
            if interset(x1, y1, queryLeft, queryRight):
                rightMax, rightMin = self.right.getMaxMinRange(queryLeft, queryRight)
                resultMax.append(rightMax)
                resultMin.append(rightMin)
        
        resultMax = getMax(resultMax)
        resultMin = getMin(resultMin)
        return resultMax, resultMin

    def update(self, value):
        if self.max < value:
            self.max = value
            self.min = value
            self.value = value
            return True
        
        isUpdated = False

        if self.value < value:
            self.value = value
            isUpdated = isUpdated or True

        if self.min < value:
            self.min = value
            isUpdated = isUpdated or True

        if self.left != None:
            if self.left.min < value:
                isUpdated = self.left.update(value) or isUpdated 

        if self.right != None:
            if self.right.min < value:
                isUpdated = self.left.update(value) or isUpdated 
        
        return isUpdated
        
    
    def toString(self):
        return json.dumps(self.toDict(), indent=4)

class MinMaxTreeFactory:
    def create(self, array, left, right):
        if len(array) == 0:
            return None
        
        n = len(array)
        index = left + n//2
        root = MinMaxTree(array[n//2], index, left, right)
        root.left = self.create(array[:n//2], left, index-1)
        root.right = self.create(array[n//2+1:], index+1, right)
        _max, _min = root.getMaxMin()
        return root

class Solution:
    def slove(self, array, year, pairs):
        factory = MinMaxTreeFactory()
        minMaxTree = factory.create(array, 0, len(array)-1)
        # TurnDownByOneIndex
        pairs = [(x-1, y-1) for x,y in pairs]
        unchangeYearStart = 1
        for currentYear, (l, r) in enumerate(pairs):
            maxValue, _minValue = minMaxTree.getMaxMinRange(l,r)
            isUpdated = minMaxTree.update(maxValue)
            if isUpdated:
                unchangeYearStart = currentYear + 1
                print(currentYear, "change")
        return unchangeYearStart

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
    test.quickTest(a.slove, ([1,2,3,4], 4, [(2,2), (2,3), (1,2), (1,3)]), 3)
    lenArray = 10**5
    randomWorstArray = [randint(-10**9, 10**9) for i in range(lenArray)]
    randomUpdatePair = []
    for i in range(lenArray):
        l = randint(1,lenArray)
        r = randint(l,min(l+160,lenArray))
        randomUpdatePair.append((l,r))
    test.quickTest(a.slove, (randomWorstArray, len(randomWorstArray), randomUpdatePair), 1)
    
if __name__ == "__main__":
    test()