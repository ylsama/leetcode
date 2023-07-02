from typing import List
import heapq
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start: int,
                       end: int) -> float:
        result = 0.
        adjTable = {}
        updated = []
        maxProbability = [0] * n
        maxProbability[start] = 1

        for index, e in enumerate(edges):
            u, v, successProbility = e[0], e[1], succProb[index]
            if u not in adjTable:
                adjTable[u] = []
            if v not in adjTable:
                adjTable[v] = []

            adjTable[u].append((v, successProbility))
            adjTable[v].append((u, successProbility))

            if u == start:
                maxProbability[v] = successProbility
                heapq.heappush(updated, (- successProbility, v))
            if v == start:
                maxProbability[u] = successProbility
                heapq.heappush(updated, (- successProbility, u))

        trace = set([start])
        for _ in range(n):
            while len(updated) > 0:
                if updated[0][1] in trace:
                    heapq.heappop(updated)
                else:
                    break
            if len(updated) == 0:
                break

            successProbility, bestPosbilityNode = heapq.heappop(updated)
            successProbility = 0 - successProbility
            if bestPosbilityNode == end:
                break
            if maxProbability[bestPosbilityNode] == 0:
                break

            trace.add(bestPosbilityNode)
            if bestPosbilityNode not in adjTable:
                continue
            for node, prob in adjTable[bestPosbilityNode]:
                currentBestProb = maxProbability[node]
                usingBestPNProb = successProbility * prob
                if currentBestProb < usingBestPNProb:
                    maxProbability[node] = usingBestPNProb
                    heapq.heappush(updated, (-usingBestPNProb, node))

        result = maxProbability[end]
        return result


def test():
    test = TestHelper()
    a = Solution()

    def compare(f1, f2):
        return abs(f1 - f2) < 0.1**5

    test.quickTest(func=a.maxProbability,
                   testInput=[3,
                              [[0, 1], [1, 2], [0, 2]],
                              [0.5, 0.5, 0.2],
                              0,
                              2],
                   testOutput=0.25000,
                   comparefunc=compare)

    test.quickTest(func=a.maxProbability,
                   testInput=[3,
                              [[0, 1], [1, 2], [0, 2]],
                              [0.5, 0.5, 0.3],
                              0,
                              2],
                   testOutput=0.30000,
                   comparefunc=compare)

    test.quickTest(func=a.maxProbability,
                   testInput=[3,
                              [[0, 1]],
                              [0.5],
                              0,
                              2],
                   testOutput=0.00000,
                   comparefunc=compare)

    test.quickTest(func=a.maxProbability,
                   testInput=[5,
                              [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
                              [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
                              3,
                              4],
                   testOutput=0.21390,
                   comparefunc=compare)

    test.quickTest(func=a.maxProbability,
                   testInput=[5,
                              [[2, 3], [1, 2], [3, 4], [1, 3], [1, 4],
                                  [0, 1], [2, 4], [0, 4], [0, 2]],
                              [0.06, 0.26, 0.49, 0.25, 0.2,
                                  0.64, 0.23, 0.21, 0.77],
                              0,
                              3],
                   testOutput=0.16000,
                   comparefunc=compare)

    test.fileTest(func=a.maxProbability,
                  testFileInput="test/1514/1.inp",
                  testFileOutput="test/1514/1.out",
                  comparefunc=compare)


if __name__ == "__main__":
    test()
