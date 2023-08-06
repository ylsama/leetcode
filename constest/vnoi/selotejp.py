"""
Ref https://oj.vnoi.info/problem/coci2021_r3_selotejp
Cho 1 mang n x m

Examlpe: n = 3, m = 4
#.##
####
#.##


Tinh so bang dinh can de phu toan bo so o #
Bang dinh dan doc | hoac dan ngang --- co the noi dai den o ke tiep

Example result: 4
"""
from typing import List


def solution_old(n: int, m: int, a: List[str], isVertical=None, cache=None):
    if cache is None:
        cache = {}
        n = n - 1
        m = m - 1

    if isVertical is not None:
        if (n, m, isVertical) in cache:
            return cache[(n, m, isVertical)]

    if n == -1:
        return 0

    if n == 0 and m == 0:
        if a[n][m] == '.':
            return 0
        else:
            return 1

    if n == 0:
        possible = []
        if a[n][m] == ".":
            possible.append(solution(n, m-1, a, True, cache))
            possible.append(solution(n, m-1, a, False, cache))

            cache[(n, m, True)] = cache[(n, m, False)] = min(possible)
            return cache[(n, m, True)]

        possible = []
        if a[n][m-1] == '.':
            possible += [solution(n, m-1, a, False, cache) + 1]
            possible += [solution(n, m-1, a, True, cache) + 1]
        else:
            possible += [solution(n, m-1, a, False, cache)]
            possible += [solution(n, m-1, a, True, cache) + 1]
        cache[(n, m, False)] = min(possible)

        possible = []
        possible += [solution(n, m-1, a, False, cache) + 1]
        possible += [solution(n, m-1, a, True, cache) + 1]
        cache[(n, m, True)] = min(possible)

    if n > 0 and m == 0:
        possible = []
        if a[n][m] == ".":
            possible += [solution(n-1, m, a, False, cache)]
            possible += [solution(n-1, m, a, True, cache)]

            cache[(n, m, True)] = cache[(n, m, False)] = min(possible)
            return cache[(n, m, True)]

        possible = []
        possible += [solution(n-1, m, a, False, cache) + 1]
        possible += [solution(n-1, m, a, True, cache) + 1]
        cache[(n, m, False)] = min(possible)

        possible = []
        if a[n-1][m] == '.':
            possible += [solution(n-1, m, a, False, cache) + 1]
            possible += [solution(n-1, m, a, True, cache) + 1]
        else:
            possible += [solution(n-1, m, a, False, cache) + 1]
            possible += [solution(n-1, m, a, True, cache)]
        cache[(n, m, True)] = min(possible)

    if n > 0 and m > 0:
        possible = []
        if a[n][m] == ".":
            possible += [solution(n, m-1, a, False, cache)]
            possible += [solution(n, m-1, a, True, cache)]
            possible += [solution(n-1, m, a, False, cache)]
            possible += [solution(n-1, m, a, True, cache)]
            cache[(n, m, True)] = cache[(n, m, False)] = min(possible)
            return cache[(n, m, True)]

        possible = []
        if a[n-1][m] == '.':
            possible += [solution(n-1, m, a, False, cache) + 1]
            possible += [solution(n-1, m, a, True, cache) + 1]
        else:
            possible += [solution(n-1, m, a, False, cache) + 1]
            possible += [solution(n-1, m, a, True, cache)]
        cache[(n, m, True)] = min(possible)

        possible = []
        if a[n][m-1] == '.':
            possible += [solution(n, m-1, a, True, cache) + 1]
            possible += [solution(n, m-1, a, False, cache) + 1]
        else:
            possible += [solution(n, m-1, a, True, cache) + 1]
            possible += [solution(n, m-1, a, False, cache)]
        cache[(n, m, False)] = min(possible)

    return min(cache[(n, m, True)], cache[(n, m, False)])


def solution(n, m, a):
    cache = {}

    def helper(i, j, mask=None):
        if i == 0 and j == 0:
            if a[i][j] == '.':
                return 0
            else:
                return 1

        if mask is not None:
            return cache[(i, j)][mask]

        last = None
        if j > 0:
            last = [i, j-1]
            helper(*last)
        elif i > 0:
            last = (i-1, m-1)
            helper(*last)

        assert last is not None

        cache[(i, j)] = []
        for mask in range(0, 1 << m):
            possible = []

            possible += [int(a[i][j] == "#")]
            possible[-1] += helper(last[0], last[1], mask)

            if j > 0:
                if (mask >> j-1) & 1 == 0 and a[i][j-1] == a[i][j] == "#":
                    possible += [helper(last[0], last[1], mask)]
            if i > 0:
                if (mask >> j) & 1 == 1 and a[i-1][j] == a[i][j] == "#":
                    possible += [helper(last[0], last[1], mask)]
            cache[(i, j)] += [min(possible)]
        return min(cache[(i, j)])

    helper(n-1, m-1)

    return min(cache[(n-1, m-1)])


if __name__ == "__main__":
    n = 4
    m = 3
    a = ["...",
         "###",
         ".#.",
         ".#.",]
    print("Test 2 is", 2 == solution(n, m, a))
    n = 1
    m = 12
    a = [".#.###.#..##"]

    print("Test 1 is", 4 == solution(n, m, a))
    print("Test 1 is", 4 == solution(m, n, [[i] for i in a[0]]))
    n = 1
    m = 9
    a = [".#.###.#."]
    print("Test 1 is", 3 == solution(n, m, a))
    print("Test 1 is", 3 == solution(m, n, [[i] for i in a[0]]))
    n = 1
    m = 6
    a = [".#.###"]

    print("Test 1 is", 2 == solution(n, m, a))
    print("Test 1 is", 2 == solution(m, n, [[i] for i in a[0]]))
    n = 2
    m = 9
    a = [".#.###.#.",
         "###...###"]
    print("Test 2 is", 5 == solution(n, m, a))
    n = 4
    m = 3
    a = [".#.",
         "###",
         ".##",
         ".#.",]
    print("Test 2 is", 3 == solution(n, m, a))
    n = 4
    m = 3
    a = [".#.",
         "###",
         ".#.",
         ".#.",]
    print("Test 2 is", 3 == solution(n, m, a))
