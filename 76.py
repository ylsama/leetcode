"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".

The testcases will be generated such that the answer is unique.
"""


class Solution:
    def toNum(self, char):
        if ord(char) <= ord("Z"):
            return ord(char) - ord("A") + 27
        return ord(char) - ord("a")

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        count = [[0]*(27*2) for i in range(n+1)]
        count_t = [0]*(27*2)

        for c in t:
            num = self.toNum(c)
            count_t[num] += 1

        for i in range(1, n+1):
            c = s[i-1]
            num = self.toNum(c)
            count[i][num] += 1
            for j in range(27*2):
                count[i][j] += count[i-1][j]

        start = -1
        end = -1
        left = -1
        for right in range(1, n+1):
            check = True
            while check:
                for j in range(27*2):
                    if count[right][j] - count[left+1][j] - count_t[j] < 0:
                        check = False
                        break
                if not check:
                    continue
                left += 1

                tStart = left
                tEnd = right
                if start == -1:
                    start, end = tStart, tEnd
                else:
                    if end - start > tEnd - tStart:
                        start, end = tStart, tEnd

        if start == -1:
            return ""
        return s[start: end]
