"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.
"""

"""
A recusive problem, with weird way of describe
1. We are given a initial string "1" = currentCountAndSay(1)
2. Then with each recusive call to caculate -> CountAndSay(i)
    2.1. We count every number in CountAndSay(i-1)
    2.2. Return:
            string(count_number[1]) <concat> number[1] <concat> ... 
    2.3. Loop until all number in currentCountAndSay string is process
"""
class Solution:
    def countChar(self, startIndex, char, countAndSayString):
        endIndex = None
        count = 0
        isFound = False
        
        if countAndSayString[startIndex] != char:
            return count, endIndex, isFound
        
        isFound = True
        for index in range(startIndex, len(countAndSayString)+1):
            if index >= len(countAndSayString):
                endIndex = index
                break
            if countAndSayString[index] != char:
                endIndex = index
                break
                
        count = endIndex - startIndex
        return count, endIndex, isFound

    def findNextCountAndSay(self, countAndSayString):
        MAX_LOOP = len(countAndSayString)
        
        nextCountAndSay = ""
        char = countAndSayString[0]
        startIndex = 0
        
        for i in range(MAX_LOOP):
            count, endIndex, isFound = self.countChar(startIndex, char, countAndSayString)

            if isFound:
                nextCountAndSay = nextCountAndSay + str(count) + char
            else:
                raise "WTF"

            if endIndex < len(countAndSayString):
                startIndex = endIndex
                char =  countAndSayString[endIndex]
            else:
                break
        return nextCountAndSay
            
    def countAndSay(self, n: int) -> str:
        result = "1"
        currentCountAndSay = result
        
        for i in range(1, n):
            currentCountAndSay = self.findNextCountAndSay(currentCountAndSay)
        result = currentCountAndSay
            
        return result

a = Solution()
print(a.countAndSay(6))