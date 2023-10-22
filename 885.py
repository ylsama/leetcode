from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        x, y, dx, dy = rStart, cStart, 0 , 1
        trace = [[0 for i in range(cols)] for i in range(rows)]
        trace[x][y] = 1
        index = 1
        result = []
        result.append([x,y])
        for i in range(900):
            for j in range(2):
                t = i
                while t>=0:
                    t -= 1
                    x, y = x + dx, y + dy
                    if 0 <= x < rows and 0<= y <cols:
                        index += 1
                        trace[x][y] = index
                        result.append([x,y])
                        if index == cols*rows:
                            for i in trace:
                                print(i)
                            return result
                if dx == 0:
                    dx, dy = dy, 0
                else:
                    dx, dy = 0, 0 - dx
        return result
    
if __name__=="__main__":
    a = Solution()
    result = a.spiralMatrixIII(10,9,3,3)