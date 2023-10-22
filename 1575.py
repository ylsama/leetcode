from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def countRoutes(self, locations: List[int], start: int,
                    finish: int, fuel: int) -> int:
        def length(city_pair):
            source, destination = city_pair
            return abs(locations[destination] - locations[source])

        def count(source, totalFuel):
            if (source, totalFuel) in totalWay:
                return totalWay[(source, totalFuel)]
            if totalFuel > fuel:
                return 0

            result = 0
            if source == finish:
                result += 1
            for destination in range(totalCity):
                if destination == source:
                    continue
                distance = length((source, destination))
                result += count(destination, totalFuel + distance)
                result %= (10**9+7)
            totalWay[(source, totalFuel)] = result
            return result

        totalWay = {}
        totalCity = len(locations)

        result = count(start, 0)
        return result

    def countRoutes_sane(self, locations: List[int], start: int,
                         finish: int, fuel: int) -> int:
        totalWay = [[0] * (fuel+1) for _ in locations]
        for i in range(fuel + 1):
            totalWay[finish][i] = 1
        city_pair = []
        totalCity = len(locations)
        for source in range(totalCity):
            for destination in range(totalCity):
                if source == destination:
                    continue
                city_pair.append((source, destination))

        def length(city_pair):
            source, destination = city_pair
            return abs(locations[destination] - locations[source])

        city_pair.sort(key=length)
        for currentFuel in range(fuel+1):
            for source, destination in city_pair:
                distance = length((source, destination))
                if currentFuel < distance:
                    break
                totalWay[source][currentFuel] += totalWay[destination][currentFuel - distance]
                totalWay[source][currentFuel] %= (10**9+7)
        return totalWay[start][fuel]


def test():
    test = TestHelper()
    a = Solution()
    locations = [2, 3, 6, 8, 4]
    start = 1
    finish = 3
    fuel = 5
    out = 4
    test.quickTest(a.countRoutes, [locations, start, finish, fuel], out)
    locations = [4, 3, 1]
    start = 1
    finish = 0
    fuel = 6
    out = 5
    test.quickTest(a.countRoutes, [locations, start, finish, fuel], out)
    locations = [5, 2, 1]
    start = 0
    finish = 2
    fuel = 3
    out = 0
    test.quickTest(a.countRoutes, [locations, start, finish, fuel], out)
    locations = [1, 2, 3]
    start = 0
    finish = 2
    fuel = 40
    out = 615088286
    test.quickTest(a.countRoutes, [locations, start, finish, fuel], out)


if __name__ == "__main__":
    test()
