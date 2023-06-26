# 1. Create a left heap and right heap
# 2. Push cost[0:candidates] to left heap and cost[len-1 - candidates : len] to
# right heap
# 3. Pop ether head of left and right heap then push next correspond from cost
# table back to the heap
# 4. Run it k time

from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = []
        right = []

        for value in costs[:candidates]:
            heapq.heappush(left, value)
        for value in costs[max(candidates, len(costs) - candidates):]:
            heapq.heappush(right, value)

        pointerLeft = candidates - 1
        pointerRight = len(costs) - candidates
        total = 0
        for i in range(k):
            if left == [] and right == []:
                break

            if left == []:
                total += heapq.heappop(right)
                continue
            elif right == []:
                total += heapq.heappop(left)
                continue

            if left[0] <= right[0]:
                total += heapq.heappop(left)
                if pointerLeft + 1 < pointerRight:
                    pointerLeft += 1
                    heapq.heappush(left, costs[pointerLeft])
            else:
                total += heapq.heappop(right)
                if pointerLeft < pointerRight - 1:
                    pointerRight -= 1
                    heapq.heappush(right, costs[pointerRight])

        return total


def test():
    a = Solution()
    a.totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4)
    a.totalCost(costs=[1, 2, 4, 1], k=3, candidates=3)


test()
