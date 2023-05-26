from typing import List
# from math import max


class Solution:
    # def bfs(self, step, m, index):
    #     if self.n - index < 2*m:
    #         self.result[step][m][index] = sum(self.piles[index:])
    #         return sum(self.piles[index:])
    #     for x in range(1, max(2*m, self.n)):
    #         minScore = 100 * 10**4
    #         if self.result[(step +1) % 2][max(m,x)][x] < 0:
    #             self.bfs((step +1) % 2, max(m,x), x)
    #         if minScore < self.result[(step +1) % 2][max(m,x)][x]:
    #             minScore = self.result[(step +1) % 2][max(m,x)][x]
    #     self.result[step][m][index] = sum(self.piles[index:]) - minScore
    #     return sum(self.piles[index:]) - minScore

    
        # stack = [(0,1,0)]
        # while stack.__len__()>0:
        #     step, m, index = stack.pop()
        #     check_stuck = False 
        #     if self.n - index < 2*m:
        #         self.result[step][m][index] = sum(self.piles[index:])
        #         continue
        #     for x in range(1, max(2*m, self.n - index)):
        #         minScore = 100 * 10**4
        #         if self.result[(step +1) % 2][max(m,x)][index + x] < 0:
        #             check_stuck = True
        #             stack.append((step , m, index))
        #             stack.append(((step +1) % 2, max(m,x), index + x))
        #             break
        #         if minScore > self.result[(step +1) % 2][max(m,x)][index + x]:
        #             minScore = self.result[(step +1) % 2][max(m,x)][index + x]

        #     if check_stuck:
        #         continue
        #     self.result[step][m][index] = sum(self.piles[index:]) - minScore
        # self.bfs(0, 1, 0)
    
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        if n == 1:
            return piles[0]
        self.n = n
        self.piles = piles
        self.result = [[-1 for index in range(n)]  for m in range(n)]
        self.trace = [[[-1,-1] for index in range(n)]  for m in range(n)]
        for m in range(n-1,0,-1):
            for index in range(n-1,-1,-1):
                if self.n - index <= 2*m:
                    self.result[m][index] = sum(self.piles[index:])
                    continue
                maxScore = 0
                for x in range(1, 2*m+1):
                    if index + x >= n:
                        continue
                    if self.result[max(m,x)][index + x] > 0:
                        if maxScore < sum(self.piles[index:]) - self.result[max(m,x)][index + x]:
                            maxScore = sum(self.piles[index:]) - self.result[max(m,x)][index + x]
                            self.trace[m][index] = [max(m,x), index+ x]
                self.result[m][index] =  maxScore
        return self.result[1][0] 

if __name__=="__main__":
    a = Solution()
    result = a.stoneGameII([1])
    print(result,  result == 1 )
    result = a.stoneGameII([1, 1, 1])
    print(result,  result == 2 )
    result = a.stoneGameII([1,2])
    print(result,  result == 3 )
    result = a.stoneGameII([2,7,9,4,4])
    print(result,  result == 10 )