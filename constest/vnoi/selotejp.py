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
import os


def solution(n, m, a):
    cache = {}

    def helper(i, j, mask):
        if i == 0 and j == 0:
            if a[i][j] == '.':
                return 0
            else:
                return 1
        return cache[(i, j)][mask]

    for i in range(n):
        for j in range(m):
            last = None
            if j > 0:
                last = [i, j-1]
            elif i > 0:
                last = (i-1, m-1)

            if last is None:
                continue
            cache[(i, j)] = []
            for mask in range(0, 1 << m):
                possible = []

                possible += [int(a[i][j] == "#")]
                possible[-1] += helper(last[0], last[1], mask)

                possible += [int(a[i][j] == "#")]
                possible[-1] += helper(last[0], last[1], mask ^ (1 << j))
                if j > 0:
                    if (mask >> j) & 1 == (mask >> j-1) & 1 == 0 and a[i][j-1] == a[i][j] == "#":
                        possible += [helper(last[0], last[1], mask)]
                        possible += [helper(last[0], last[1], mask ^ (1 << j))]
                if i > 0:
                    if (mask >> j) & 1 == 1 and a[i-1][j] == a[i][j] == "#":
                        possible += [helper(last[0], last[1], mask)]
                cache[(i, j)] += [min(possible)]

    return min(cache[(n-1, m-1)])


def read_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract n and m from the first line
    n, m = map(int, lines[0].split())

    # Extract the 2D array 'a' from the rest of the lines
    a = [line.strip() for line in lines[1:]]

    return n, m, a


def read_output_from_file(filename):
    with open(filename, 'r') as file:
        output = file.read().strip()

    return int(output)


def check_solution(input_file, output_file):
    n, m, a = read_input_from_file(input_file)
    if (n * m * 1 << m) > 10000000:
        return True
    expected_output = read_output_from_file(output_file)

    # Compare the expected output with your solution
    output = solution(n, m, a)
    print(input_file, output, expected_output)
    return output == expected_output


def read_input_from_user():
    n, m = map(int, input().split())

    a = [input().strip() for _ in range(n)]

    return n, m, a


def main():
    n, m, a = read_input_from_user()
    print(solution(n, m, a))


def fileTest():
    folder_path = "test/"

    file_list = os.listdir(folder_path)

    input = []
    for file in file_list:
        if "in" in file:
            input.append([os.path.join(folder_path, file), os.path.join(
                folder_path, file.replace("in", "out"))])

    for input_file, output_file in input:
        is_solution_correct = check_solution(input_file, output_file)
        print(f"{input_file}: {'Correct' if is_solution_correct else 'Incorrect'}")


def test():
    inf = r"test/selotejp.dummy.in.3"
    outf = inf.replace("in", "out")
    input = read_input_from_file(inf)
    output = read_output_from_file(outf)
    print("Test dummy is", output, solution(*input))

    n = 4
    m = 3
    a = ["###",
         "#.#",
         "##.",
         ".#.",]
    print("Test 2 is", 4 == solution(n, m, a))
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


if __name__ == "__main__":
    # main()
    test()
    fileTest()
