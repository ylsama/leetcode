from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = [-1 for i in range(n*m)]
        trace = [[True for i in range(n)] for i in range(m)]
        x, y, dx, dy = 0, 0, 0 , 1
        for index in range(0,n*m):
            result[index] = matrix[x][y]
            trace[x][y] = False
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and  0 <= ny < n:
                if trace[nx][ny]:
                    x, y = nx, ny
                    continue
            if dx == 0:
                dx, dy = dy, 0
            else:
                dx, dy = 0, 0 - dx
            nx, ny = x + dx, y + dy
            x, y = nx, ny
        return result


if __name__=="__main__":
    a = Solution()
    result = a.generateMatrix_2([[43, 44, 45, 46, 47, 48, 49, 50, 65], [42, 21, 22, 23, 24, 25, 26, 51, 66], [41, 20, 7, 8, 9, 10, 27, 52, 67], [40, 19, 6, 1, 2, 11, 28, 53, 68]
[39, 18, 5, 4, 3, 12, 29, 54, 69], [38, 17, 16, 15, 14, 13, 30, 55, 70], [37, 36, 35, 34, 33, 32, 31, 56, 71], [64, 63, 62, 61, 60, 59, 58, 57, 72], [81, 80, 79, 78, 77, 76, 75, 74, 73], [90, 89, 88, 87, 86, 85, 84, 83, 82]])
    for i in result:
        print(i)