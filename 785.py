from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        nodeColorSet = [set(), set()]
        queue = [(0,0)]
        trace = set()
        for i in range(n):
            trace.add(i)
        while len(queue)>0:
            u, color = queue.pop(0)
            if u in trace:
                trace = trace - set([u])
                for v in graph[u]:
                    if v in nodeColorSet[color]:
                        return False
                    else:
                        new_color = 0
                        if color == new_color:
                            new_color = 1
                        nodeColorSet[new_color].add(v)
                        queue.append((v,new_color)) 
                
            if len(queue) == 0 and len(trace) != 0:
                queue.append((next(iter(trace)),0))
        return True

if __name__=="__main__":
    a = Solution()
    graph = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
    result = a.isBipartite(graph)
    print(result)
