import uuid
import time
from math import trunc 

class TestCase:
    def __init__(self, testInput, testOutput, testName : str = None, id = None):
        if not id:
            self.id = uuid.uuid4()
        else:
            self.id = id
        if not testName:
            self.name = self.id
        else:
            self.name = testName
        self.input = testInput
        self.output = testOutput

    def toString(self):
        if self.name:
            return self.name
        return self.id

class TestHelper:
    def __init__(self):
        self.testSet = []
    
    def addTest(self,  testInput, testOutput, testName = None, testId = None):
        if not testId:
            testId = len(self.testSet)
        newTestCase = TestCase(testInput, testOutput, testName, testId)
        self.testSet.append(newTestCase)
        return newTestCase.toString()
    
    def addTestCase(self, testCase):
        self.testSet.append(testCase)

    def checkDefinedTest(self, func):
        for testCase in self.testSet:
            out = func(*testCase.input)
            print(f"Test {testCase.toString()} is {out == testCase.output}")

    def getRunTime(self, functionCall):
        start = time.time()
        functionCall
        end = time.time()
        return end - start 
    
    def quickTest(self, func, testInput, testOutput, testName = None, addTest = False, showInputLength = 20):
        if addTest:
            self.addTest(testInput, testOutput, testName)
        
        if not testName:
            testName = "quickTest"
        
        start = time.time()
        out = func(*testInput)
        end = time.time()

        if out != testOutput:
            print(f"Test {testName}, func: \"{func.__name__}\", input: \"{str(testInput)[:showInputLength*4]}\" is {out == testOutput}, Running time = {trunc((end - start)*1000000) / 1000.} ms")
            # Rerun
            # func(*testInput)
        else:
            print(f"Test {testName}, func: \"{func.__name__}\", input: \"{str(testInput)[:showInputLength]}\" is {out == testOutput}, Running time = {trunc((end - start)*1000000) / 1000.} ms")


    def quickTestCase(self, func, testCase: TestCase, addTestCase = True):
        if addTestCase:
            self.addTestCase(func, testCase)
        
        out = func(*testCase.Input)
        print(f"Test {testCase.name} is {out == testCase.input}")


def main():
    def add(x,y):
        return x+y
    test = TestHelper()
    test.addTest((1,1),2, "Example 1")
    test.addTest((1,2),3, "Example 2")
    test.addTest((21,2),23, "Example 3")
    test.addTest((2001,2),2003)
    test.addTest((201,2),203)
    test.checkDefinedTest(add)
    test.quickTest(add,(1,2),3)
    test.quickTest(add,(5,2),7)
    test.quickTest(add,(1,5),6)
    test.quickTest(add,(6,5),11)
    
if __name__=="__main__":
    main()
