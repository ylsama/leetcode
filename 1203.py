from typing import List


class Solution:
    def canFinish(self, node, graph) -> bool:
        is_safe_node = [None] * len(graph)

        def DFS(current_node_id):
            if is_safe_node[current_node_id] is not None:
                return is_safe_node[current_node_id]

            is_safe_node[current_node_id] = False
            for adj_node_id in graph[current_node_id]:
                if DFS(adj_node_id) == False:
                    return False

            is_safe_node[current_node_id] = True
            return True

        for course_id in node:
            if not DFS(course_id):
                return False
        return True

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        print(self.canFinish(list(range(n)), beforeItems))
        groupNode = [[] for _ in range(m + 1)]
        groupAdj = [[] for _ in range(n)]
        for i, n in enumerate(group):
            groupNode[n] += [i]
            if n == -1:
                group[i] = m + len(groupNode[-1])

            if group[i] < m and len(groupNode[group[i]]) > 0:
                tmp = beforeItems[i] + groupAdj[groupNode[group[i]][0]]

                for member in groupNode[group[i]]:
                    groupAdj[member] = tmp
            else:
                groupAdj[i] = beforeItems[i]

        return []


a = Solution()
res = a.sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
                  beforeItems=[[], [6], [5], [6], [3, 6], [], [], []])


print(res == [6, 3, 4, 1, 5, 2, 0, 7])
res = a.sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
                  beforeItems=[[], [6], [5], [6], [3], [], [4], []])
print(res)
