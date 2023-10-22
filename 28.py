class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        

if __name__=="__main__":
    a = Solution()
    result = a.strStr(haystack = "leetcode", needle = "leeto")
    print(result)

    result = a.strStr(haystack = "sadbutsad", needle = "sad")
    print(result)
    