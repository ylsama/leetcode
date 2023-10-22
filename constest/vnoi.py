from national.testHelper import TestHelper


def vnoj(moneys):
    n = len(moneys)
    if n == 0:
        return 0
    if n == 1:
        return moneys[0] * 2
    moneys.sort()

    def findMidPoint(r):
        mid = 0
        for i in range(r):
            mid = i
            if sumArr[i] >= sumArr[r]-sumArr[i]:
                break
        return mid

    def helper(moneys):
        d = {}
        for i in moneys:
            for k in d:
                if k not in d:
                    d[k] = 0
    possible = []

    possible += []

    return sum(moneys)


test = TestHelper()

test.quickTest(vnoj, [[1, 2, 3, 6]], 6)
test.quickTest(vnoj, [[2, 3, 5, 8, 13]], 18)
test.quickTest(vnoj, [[2, 2, 3, 5, 3, 2]], 18)
