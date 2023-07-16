from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def find_rarest_skill(self, candidates, skill_set, not_needed_skill):
        skill_talent = {}
        for candidate in candidates:
            for skill in skill_set[candidate]:
                if skill not in skill_talent:
                    skill_talent[skill] = []
                skill_talent[skill].append(candidate)

        rarest_skill = None

        for skill in skill_talent:
            if skill in not_needed_skill:
                continue
            if rarest_skill is None:
                rarest_skill = skill
            elif len(skill_talent[rarest_skill]) > len(skill_talent[skill]):
                rarest_skill = skill

        return rarest_skill, set(skill_talent[rarest_skill])

    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        queue = [(set(range(len(people))), set())]
        while queue:
            available_people, current_team_skill = queue.pop(0)
            if available_people is None:
                return [i for i in len(people)]
            if len(current_team_skill) == len(req_skills):
                return list(set(range(len(people))).difference(available_people))

            _, talented_peoples = self.find_rarest_skill(
                available_people, people, current_team_skill)

            for candidate in talented_peoples:
                team_skill = current_team_skill.union(set(people[candidate]))
                remain_people = available_people.copy()
                remain_people.remove(candidate)
                queue.append((remain_people, team_skill))
                if len(team_skill) == len(req_skills):
                    queue = [queue[-1]]
                    break

        return [i for i in len(people)]


def test():
    test = TestHelper()
    a = Solution()

    test.fileTest(a.smallestSufficientTeam,
                  testFileInput=r"test/1125/1.inp",
                  testFileOutput=r"test/1125/1.out")


if __name__ == "__main__":
    test()
