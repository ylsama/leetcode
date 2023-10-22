"""
# PROBLEM
744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
"""


"""
# CONCEPT TO KNOW
1. non-decreasing order
    - First find smallest character greater than target
    - If there isn't return first character in Letters
    - A binary search is fine enough

2. Character comparing:
    - Everything is presented in computer as numberic value. By defining a character set (or we can call encode), we bind
                number      ->       character
    
    - Normaly, computer working on a acsii character table (8 bit value). Most of application today using UTF-8, Window used different character set call Wind-1523 or what ever.
    
    ## Any encode table
        toNumber(character, encode) -> int:
        toChar(number, encode) -> char:
    ## Acsii only
        getAcsiiIndex(char) -> int
        acsiiIndexToChar(int) -> char
    
    - So, by default, we use their numberic value to compare, sort, binary search on character, that all
    
3. Test driven
    - The code should be test, to make sure any change will not break any logic
    - Here I try to implement some class to handle test, better than just print out non-sence
and thearically being reuse able for other code
    - I code some simple Test, TestCase class to keep all Test case the infomation
    
4. Binary search
    On a sorted (non-decreasing order) array, we can use the fact that
            item_1_index <= item_2_index  =>  item_1_value <= item_2_value
    to quickly search and find our wanted value in the array or not
    
    When trying to find: target
    - Assuming, target_index is the index if target in our sorted array
    - We set up our rule
            left_index <= target_index < right_index
            left_value <= target       < right_value 
            
    - So by minimize right_index 
            maximize left_value
    We will have right_value is the needed answer
"""
from typing import List
import uuid

class Solution:
    def binarySearch(self, letters, target):
        
        def getAcsiiIndex(char):
            return ord(char)
        
        def acsiiIndexToChar(acsiiIndex):
            return chr(acsiiIndex)
        
        leftMost = -1
        rightMost = len(letters)
        
        targetValue = getAcsiiIndex(target)
        
        left = leftMost
        right = rightMost
        
        MAX_LOG_TIME = trunc(log(rightMost - leftMost,2))+1 
        for _ in range(MAX_LOG_TIME):
            mid = (left+right)//2
            if left == mid:
                break
            
            midValue = getAcsiiIndex(letters[mid])
            
            if  midValue <= targetValue:
                left = mid
            else:
                right = mid
        
        if left+1 != right:
            raise "Logic fail, can't search in O(logn) time"
        
        isFound = targetValue == getAcsiiIndex(letters[left])
        targetIndex = left
        nearestCharacterIndex = right
        
        return targetIndex, isFound, nearestCharacterIndex
        
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        firstCharacter = letters[0]
        targetIndex, isFound, nearestCharacterIndex = self.binarySearch(letters, target)
        
        result = firstCharacter
        if nearestCharacterIndex < len(letters):
            result = letters[nearestCharacterIndex]
            
        return result


class TestCase:
    def __init__(self, testInput, testOutput, testName = None):
        if testName:
            self.name = testName
        else:
            self.name = uuid.uuid4()
        self.input = testInput
        self.output = testOutput


class Test:
    def __init__(self):
        self.testSet = []
    
    def addTest(self,  testInput, testOutput, testName = None):
        newTestCase = TestCase(testInput, testOutput, testName)
        self.testSet.append(newTestCase)

    def checkTest(self, func):
        for testCase in self.testSet:
            out = func(*testCase.input)
            print(f"Test {testCase.name} is {out == testCase.output}")

def main():
    test = Test()

    letters = ["c","f","j"]
    target = "a"
    inputTest = (letters, target)
    outputTest = "c"
    test.addTest( inputTest, outputTest, "Example 1")

    letters = ["c","f","j"]
    target = "c"
    inputTest = (letters, target)
    outputTest = "f"
    test.addTest( inputTest, outputTest, "Example 2")

    letters = ["x","x","y","y"]
    target = "z"
    inputTest = (letters, target)
    outputTest = "x"
    test.addTest( inputTest, outputTest, "Example 3")

    letters = ["a","b","c","d"]
    target = "e"
    inputTest = (letters, target)
    outputTest = "a"
    test.addTest(inputTest, outputTest)
    
    letters = ["a","b","c","d"]
    target = "c"
    inputTest = (letters, target)
    outputTest = "d"
    test.addTest(inputTest, outputTest)
    
    a = Solution()
    test.checkTest(a.nextGreatestLetter)
    
if __name__=="__main__":
    main()

