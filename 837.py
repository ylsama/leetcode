from functools import cache


class Solution:
    def new21Game_deleteRecution(self, n: int, k: int, maxPts: int) -> float:
        self.result = [-1 for i in range(k+maxPts)]
        self.maxPts = maxPts
        self.n = n
        self.k = k
        for point in range(k,k + maxPts):
            if point <= self.n:
                self.result[point] = 1/(self.maxPts)
            else:
                self.result[point] = 0
        for point in range(k-1,-1,-1):
            lte_n = 1/(self.maxPts) 
            lte_res = 0
            for i in range(1,self.maxPts+1):
                lte_res += self.result[point + i]
            self.result[point] = lte_n*lte_res
            
        return self.result[0]*self.maxPts
    
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        result = [-1 for i in range(k+maxPts)]
        for point in range(k,k + maxPts):
            if point <= n:
                result[point] = 1/maxPts
            else:
                result[point] = 0
        point = k-1
        sum_odd = 0
        for i in range(1,maxPts+1):
            sum_odd += result[point + i]
        for point in range(k-1,-1,-1):
            result[point] = sum_odd / maxPts
            sum_odd = sum_odd + result[point] - result[point + maxPts]
        return result[0]*maxPts

if __name__=="__main__":
    a = Solution()
    # n = 9811
    # k = 8776
    # maxPts = 1096
    # result = a.new21Game(n, k, maxPts)
    # print(result)
    # result = a.new21Game(n = 21, k = 17, maxPts = 10)
    # print(result, abs(result - 0.73278) <= 0.00001)
    result = a.new21Game(n = 5710, k = 5070, maxPts = 8516)
    print(result, abs(result - 0.73278) <= 0.00001)

    

