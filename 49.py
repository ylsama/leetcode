"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import List

class Solution:
    """
    As we dealling with really little range of character
            strs[i] consists of lowercase English letters.
    We could do a hash where if any baseString have a same number representation; it mean they anagrams together. A sane version is just sort the baseString then return it's hash. Here i using count hash
    """
    def sortString(self, baseString):
        charactersWithCount = {}
        for char in baseString:
            if not char in charactersWithCount:
                charactersWithCount[char] = 1
            charactersWithCount[char] += 1
            
        sortedString = "" 
        for acsiiIndex in range(ord("a"),ord("z")+1):
            char = chr(acsiiIndex)
            if char in charactersWithCount:
                sortedString = sortedString + char*charactersWithCount[char]
                
        return sortedString
    
    """
    just using python hash here
    """
    def craftedHash(self, baseString):
        sortedString = self.sortString(baseString)
        pythonStringHash = sortedString.__hash__()
        return pythonStringHash
    
    """
    using our craftedHash, we could just seperating the string using dict
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultGroupAnagrams = {}
        
        for currentString in strs:
            currentCraftedHash = self.craftedHash(currentString)
            if not currentCraftedHash in resultGroupAnagrams:
                resultGroupAnagrams[currentCraftedHash] = []
            resultGroupAnagrams[currentCraftedHash].append(currentString)
            
            # This is the same as using sortedString insead of our craftedHash
            # resultGroupAnagrams[self.sortedString(currentString)].append(currentString)

        resultGroupAnagramsToList = [resultGroupAnagrams[i] for i in resultGroupAnagrams]
        return resultGroupAnagramsToList
    
def test():
    a = Solution()
    # Example 1:
    strs = ["eat","tea","tan","ate","nat","bat"]
    Output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result = a.groupAnagrams(strs)
    print("test 1 is", Output == result)
    # Example 2:
    strs = [""]
    Output = [[""]]
    result = a.groupAnagrams(strs)
    print("test 2 is", Output == result)
    # Example 3:
    strs = ["a"]
    Output = [["a"]]
    result = a.groupAnagrams(strs)
    print("test 3 is", Output == result)

    
if __name__ == "__main__":
    test()