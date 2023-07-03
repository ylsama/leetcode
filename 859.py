# from ulti.testHelper.testHelper import TestHelper


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Find different of s and goal
        if len(s) != len(goal):
            return False

        diff = []
        for i, (x, y) in enumerate(zip(s, goal)):
            if x != y:
                diff.append(i)

        if len(diff) != 0 and len(diff) != 2:
            return False

        if len(diff) == 2:
            return s[diff[1]] == goal[diff[0]] and s[diff[0]] == goal[diff[1]]

        check = set()
        for c in s:
            if c not in check:
                check.add(c)
            else:
                return True
        return False
