from typing import List
from ulti.testHelper.testHelper import TestHelper
import heapq


class Solution:
    def kSmallestPairs(self,
                       nums1: List[int],
                       nums2: List[int],
                       k: int) -> List[List[int]]:
        p1 = [(value + nums2[0], (index, 0))
              for index, value in enumerate(nums1)]
        heapq.heapify(p1)
        arr = []
        for _ in range(k):
            if len(arr) == k:
                break
            if len(p1) == 0:
                break
            _, (pos1, pos2) = heapq.heappop(p1)
            arr.append([nums1[pos1], nums2[pos2]])
            if pos2+1 < len(nums2):
                heapq.heappush(
                    p1, (nums1[pos1] + nums2[pos2+1], (pos1, pos2+1)))
        return arr


def Test():
    test = TestHelper()
    a = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    out = [[1, 2], [1, 4], [1, 6]]
    test.quickTest(a.kSmallestPairs, [nums1, nums2, k], out)
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    out = [[1, 1], [1, 1]]
    test.quickTest(a.kSmallestPairs, [nums1, nums2, k], out)
    nums1 = [1, 2]
    nums2 = [3]
    k = 3
    out = [[1, 3], [2, 3]]
    test.quickTest(a.kSmallestPairs, [nums1, nums2, k], out)
    test.quickTest(a.kSmallestPairs, [[1, 1, 2],
                                      [1, 2, 3],
                                      10], [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]])


if __name__ == "__main__":
    Test()
