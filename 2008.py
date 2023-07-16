from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rideStartAt = defaultdict(list)
        for start, end, tip in rides:
            rideStartAt[start].append([end, end - start + tip])
        lookup = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            for end, true_value in rideStartAt[i]:
                lookup[i] = max(lookup[i], lookup[end] + true_value)
            lookup[i] = max(lookup[i], lookup[i + 1])

        return lookup[1]


class Solution_2:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        def sort_key_end(x):
            return x[1]

        rides.sort(key=sort_key_end)
        lookup = [0] * (n + 1)
        car_pos = 1
        for s, e, v in rides:
            for i in range(car_pos, e):
                lookup[i] = lookup[car_pos]
            car_pos = e
            possible = (e - s + v)
            if s > 0:
                possible += lookup[s]
            lookup[e] = max(lookup[e], lookup[e-1], possible)

        return lookup[car_pos]


class Solution_3:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        def sort_key_end(x):
            return x[1]

        rides.sort(key=sort_key_end)
        key = [-1]
        lookup = [0]

        for start, end, tip in rides:
            search = bisect_right(key, start)
            true_rides_value = lookup[search - 1] + end - start + tip
            lookup.append(max(lookup[-1], true_rides_value))
            key.append(end)
        return lookup[-1]
