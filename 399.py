from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        edges = {}
        n = len(equations)
        for i in range(n):
            a,b = equations[i]
            if not a in edges: 
                edges[a] = {}
            edges[a][b] = values[i]

            if not b in edges: 
                edges[b] = {}
            edges[b][a] = 1. / values[i]
        
        for a in edges.keys():
            edges[a][a] = 1.

        for a in edges.keys():
            queue = [a]
            trace = {}
            for i in edges.keys():
                trace[i] = True
            
            while queue:
                first = queue.pop(0)
                trace[first] = False
                for b in edges[first]:
                    if trace[b]:
                        queue.append(b)
                    if not b in edges[a]:
                        edges[a][b] = edges[a][first] * edges[first][b]

        print(edges)
        for c,d in queries:
            if c in edges:
                if d in edges[c]:
                    result.append(edges[c][d])
                    continue
            result.append(-1.)
        return result
    

if __name__=="__main__":
    a = Solution()
    result = a.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
    print(result)