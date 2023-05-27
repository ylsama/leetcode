import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = set()
        i_p = 0
        while i_p < len(p):
            char = p[i_p]
            if i_p == 0:
                if char == '.':
                    for i in range(len(s)):
                        match.add((i,i+1))
                else:
                    for i in range(len(s)):
                        if s[i] == char:
                            match.add((i,i+1))
            else:
                temp = set()
                for index, end_index in match:
                    if char == '*':
                        temp.add((index,end_index-1))
                        for i in range(max(end_index-1,0),len(s)):
                            if s[i] ==p[i_p-1] or p[i_p-1] == '.':
                                temp.add((index,i+1))
                            else:
                                break
                    elif char == '.':
                        if end_index < len(s):
                            temp.add((index, end_index+1))
                    else:
                        if end_index < len(s):
                            if s[end_index] == char:
                                temp.add((index,end_index+1))
                
                if len(temp) == 0 and i_p + 1 < len(p):
                    if p[i_p + 1] == '*':
                        i_p += 2
                        continue
                if len(match) == 0 and p[i_p] == '*':
                    for i in range(len(s)):
                        match.add((i,i))
                    i_p += 1
                    continue
                match = temp
            i_p += 1
            print("step =", i_p, (0,len(s)) in match)
        return (0,len(s)) in match

if __name__== "__main__":
    a = Solution()
    result = a.isMatch(s = "aa", p = "a")
    print(result, "\n Test 1 is ",result == False)
    result = a.isMatch(s = "aa", p = "a*")
    print(result, "\n Test 2 is ",result == True)
    result = a.isMatch(s = "ab", p = ".*")
    print(result, "\n Test 3 is ",result == True)
    result = a.isMatch(s = "abcdfghjklqew", p = ".*")
    print(result, "\n Test 4 is ",result == True)
    result = a.isMatch(s = "aba", p = "a*")
    print(result, "\n Test 5 is ",result == False)
    result = a.isMatch(s = "aba", p = "w*aba")
    print(result, "\n Test 6 is ",result == True)
    result = a.isMatch(s = "a", p = "a*")
    print(result, "\n Test 7 is ",result == True)
    result = a.isMatch(s = "b", p = ".")
    print(result, "\n Test 8 is ",result == True)
    result = a.isMatch(s = "aaaaaaaaaaaab", p = "a*b")
    print(result, "\n Test 9 is ",result == True)
    result = a.isMatch(s = "mississippi", p = "mis*is*p*.")
    print(result, "\n Test 10 is ",result == False)
    result = a.isMatch(s = "aaa", p = "ab*ac*a")
    print(result, "\n Test 11 is ",result == True)
    result = a.isMatch(s = "ab", p = ".*c")
    print(result, "\n Test 12 is ",result == False)
    result = a.isMatch(s = "a", p = ".*..a*")
    print(result, "\n Test 13 is ",result == False)
    result = a.isMatch(s = "aab", p = "c*a*b")
    print(result, "\n Test 14 is ",result == True)
    result = a.isMatch(s = "aabcbcbcaccbcaabc", p = ".*a*aa*.*b*.c*.*a*")
    print(result, "\n Test 15 is ",result == True)


