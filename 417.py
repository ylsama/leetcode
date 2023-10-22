from typing import List

class Solution:
    def getAdjNode(self, x, y):
        result = []
        dx, dy = 0, 1
        for i in range(4):
            nx , ny = x + dx, y + dy 
            if 0 <= nx < self.m and 0 <= ny < self.n:
                if self.heights[nx][ny] >= self.heights[x][y]:
                    result.append((nx, ny))
            if dx == 0:
                dx, dy = dy, 0
            else:
                dx, dy = 0, - dx
        return result
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        n = self.n
        m = self.m
        result = []

        notAdjAtlantic = [[True for i in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            q.append((i,n-1))
            notAdjAtlantic[i][n-1] = False

        for i in range(n):
            if notAdjAtlantic[m-1][i]:
                q.append((m-1,i))
                notAdjAtlantic[m-1][i] = False

        while q.__len__()>0:
            x, y = q.pop(0)
            for nx, ny in self.getAdjNode(x, y):
                if notAdjAtlantic[nx][ny]:
                    notAdjAtlantic[nx][ny] = False
                    q.append((nx, ny))
        
        notAdjPacific = [[True for i in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            q.append((i,0))
            notAdjPacific[i][0] = False

        for i in range(n):
            if notAdjPacific[0][i]:
                q.append((0,i))
                notAdjPacific[0][i] = False

        while q.__len__()>0:
            x, y = q.pop(0)
            if notAdjAtlantic[x][y] == False:
                result.append([x,y])
            for nx, ny in self.getAdjNode(x, y):
                if notAdjPacific[nx][ny]:
                    notAdjPacific[nx][ny] = False
                    q.append((nx, ny))

        return result
    


if __name__=="__main__":
    a = Solution()
    result = a.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1]])
    print(result, result == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
    result = a.pacificAtlantic(heights = [[1]])
    print(result, result == [[0,0]])
    result = a.pacificAtlantic(heights = [[2,1],[1,2]])
    print(result, result == [[0,0],[0,1],[1,0],[1,1]])
    result = a.pacificAtlantic(heights = [[1,1],[1,1],[1,1]])
    print(result)
    
