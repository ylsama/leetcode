from typing import List
from bisect import bisect_right
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def bit_1_pos(self, number):
        for pos, c in enumerate(bin(number)[2:][::-1]):
            if c == '1':
                yield pos

    def needed_skill(self, number):
        tmp = number
        pos = 0
        while tmp != 0:
            if tmp % 2 == 1:
                tmp = tmp // 2
                pos += 1
            else:
                break

        return pos

    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        words_dictinary = req_skills.copy()
        words_dictinary.sort()
        number_representation = []
        for p in people:
            craft_number = 0
            for skill in p:
                words_index = bisect_right(words_dictinary, skill) - 1
                craft_number += 1 << words_index
            number_representation.append(craft_number)

        start = 0
        last = (1 << len(people)) - 1

        best = last
        queue = [(start, 0)]
        visited = set()
        while len(queue) > 0:
            possible_combination, is_sufficient = queue.pop(0)
            visited.add(possible_combination)
            if possible_combination.bit_count() > best.bit_count():
                continue

            if is_sufficient.bit_count() == len(words_dictinary):
                best = possible_combination
                break

            needed_skill = self.needed_skill(is_sufficient)
            for index in range(len(people)):
                if (number_representation[index] >> needed_skill) % 2 == 0:
                    continue
                team_skill = is_sufficient | number_representation[index]
                if team_skill == is_sufficient:
                    continue
                team_member = possible_combination | (1 << index)
                if team_member in visited:
                    continue
                visited.add(team_member)
                queue.append((team_member, team_skill))

        return [i for i in self.bit_1_pos(best)]


def test():
    test = TestHelper()
    a = Solution()

    test.fileTest(a.smallestSufficientTeam,
                  testFileInput=r"test/1125/1.inp",
                  testFileOutput=r"test/1125/1.out")


if __name__ == "__main__":
    test()
