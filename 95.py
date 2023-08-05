from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int, words=None) -> List[Optional[TreeNode]]:
        if words is None:
            words = list(range(1, n+1))

        if len(words) == 0:
            return [None]

        res = []
        for i, v in enumerate(words):
            lefts = self.generateTrees(0, words[:i])
            rights = self.generateTrees(0, words[i+1:])
            for l in lefts:
                for r in rights:
                    res.append(TreeNode(v, l, r))

        print(res)
        return res


if __name__ == "__main__":
    a = Solution()
    a.generateTrees(2)
    a.generateTrees(4)
