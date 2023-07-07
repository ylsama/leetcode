from ulti.testHelper.testHelper import TestHelper


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxLen = 0

        lastTrue = [-1]*(k+1)
        currLastTrue = 0

        lastFalse = [-1]*(k+1)
        currLastFalse = 0

        for index, answer in enumerate(answerKey):
            if answer == 'T':
                lastTrue[currLastTrue] = index
                currLastTrue += 1
                currLastTrue %= k + 1
            else:
                lastFalse[currLastFalse] = index
                currLastFalse += 1
                currLastFalse %= k + 1

            possibleMaxLen = []
            possibleMaxLen.append(index - lastFalse[currLastFalse])
            possibleMaxLen.append(index - lastTrue[currLastTrue])
            possibleMaxLen.append(maxLen)

            maxLen = max(possibleMaxLen)

        return maxLen


def test():
    test = TestHelper()
    a = Solution()
    test.quickTest(a.maxConsecutiveAnswers, ["TTFF", 2], 4)
    test.quickTest(a.maxConsecutiveAnswers, ["TFTFF", 2], 5)
    test.quickTest(a.maxConsecutiveAnswers, ["TFFFTTFF", 2], 7)
    test.quickTest(a.maxConsecutiveAnswers, ["TTTTTFF", 1], 6)


if __name__ == "__main__":
    test()
