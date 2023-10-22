"""
956. Tallest Billboard

You are installing a billboard and want it to have the largest height.
The billboard will have two steel supports, one on each side. Each
steel support must be an equal height.

You are given a collection of rods that can be welded together. For
example, if you have rods of lengths 1, 2, and 3, you can weld them
together to make a support of length 6.

Return the largest possible height of your billboard installation.
If you cannot support the billboard, return 0.

1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000
"""
from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        bestHight = {}
        bestHight[(0, 0)] = 0

        for r in rods:
            possible = []
            for knowdBest in bestHight:
                x, y = knowdBest
                possible.append(((x+r, y), bestHight[knowdBest]))
                possible.append(((x, y+r), bestHight[knowdBest]))
                if y >= r:
                    possible.append(((x, y-r), bestHight[knowdBest] + r))
                if x >= r:
                    possible.append(((x - r, y), bestHight[knowdBest] + r))

            for (px, py), ph in possible:
                if (px, py) not in bestHight:
                    bestHight[(px, py)] = ph
                    continue
                if bestHight[(px, py)] < ph:
                    bestHight[(px, py)] = ph
        return bestHight[(0, 0)]


def test():
    test = TestHelper()
    a = Solution()

    test.quickTest(a.tallestBillboard, [[1, 2, 3, 6]], 6)
    test.quickTest(a.tallestBillboard, [[1, 2, 3, 4, 5, 6]], 10)
    test.quickTest(a.tallestBillboard, [[1, 2]], 0)


if __name__ == "__main__":
    test()
