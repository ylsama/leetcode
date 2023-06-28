from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def findMaxProabilityNode(self, trace, n, start, maxProb):
        currBestNode = -1

        for node in range(n):
            if node == start or node in trace:
                continue
            if currBestNode == -1:
                currBestNode = node
            elif maxProb[node] > maxProb[currBestNode]:
                currBestNode = node

        return currBestNode

    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start: int,
                       end: int) -> float:
        def manualHash(u, v):
            if u < v:
                return (u, v).__hash__()
            return (v, u).__hash__()

        result = 0.
        quickRef = {}
        maxProbability = [0] * n
        maxProbability[start] = 1

        for index, e in enumerate(edges):
            u, v, successProbility = e[0], e[1], succProb[index]
            quickRef[manualHash(u, v)] = successProbility
            if u == start:
                maxProbability[v] = successProbility
            if v == start:
                maxProbability[u] = successProbility

        trace = set()
        for _ in range(n):
            bestPosbilityNode = self.findMaxProabilityNode(trace,
                                                           n,
                                                           start,
                                                           maxProbability)
            if bestPosbilityNode == end:
                break
            if maxProbability[bestPosbilityNode] == 0:
                break

            trace.add(bestPosbilityNode)
            for node in range(n):
                if manualHash(bestPosbilityNode, node) not in quickRef:
                    continue
                currMax = maxProbability[node]
                usingBestPNProb = maxProbability[bestPosbilityNode] * \
                    quickRef[manualHash(bestPosbilityNode, node)]
                if currMax < usingBestPNProb:
                    maxProbability[node] = usingBestPNProb

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


if __name__ == "__main__":
    test()
