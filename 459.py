from ulti.testHelper.testHelper import TestHelper


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        visited = [False] * n
        for i in range(1, n):
            if visited[i]:
                continue
            visited[i] = True
            if n % i != 0:
                continue

            sub = s[:i]
            res = True
            for step in range(n//i):
                if sub != s[step*i: (step+1) * i]:
                    res = False
                    break
            if res:
                return True

        return False


if __name__ == "__main__":
    a = Solution()
    input = ["aaaaaab"]
    output = False

    t = TestHelper()
    t.quickTest(a.repeatedSubstringPattern, testInput=input,
                testOutput=output, testName="Example 1")
    test = "qhasdnjwkldjqwpduasczxcnbasioqwuyebabcqwqsac"
    for i in range(7):
        test += test[:-1] + test[-1:]
    test += "a" * 4368
    t.quickTest(a.repeatedSubstringPattern, testInput=[test],
                testOutput=False, testName="Example 2")
