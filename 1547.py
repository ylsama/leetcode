from functools import cache
from typing import List


class Solution:
    def find_min_cost(self, left, right, cuts_left, cuts_right):
        if self.total_cost_table[left][right] != -1:
            return self.total_cost_table[left][right]
        
        if len(self.cuts[cuts_left: cuts_right]) == 0:
            self.total_cost_table[left][right] = 0
            return 0
        
        if len(self.cuts[cuts_left: cuts_right]) == 1:
            self.trace_table[left][right] =  cuts_left
            self.total_cost_table[left][right] = right - left
            return right - left
        
        cost = right - left
        min_cut_index = cuts_left
        min_cut = self.cuts[min_cut_index]
        # caculate the cost using recusive call of minCost, as we will want to
        # solve 2 remainning array
        min_total_cost = cost + self.find_min_cost(left, min_cut, cuts_left, min_cut_index) + self.find_min_cost(min_cut, right, min_cut_index+1, cuts_right)
        for try_cut_index in range(cuts_left, cuts_right):
            try_cut = self.cuts[try_cut_index]
            try_cut_cost = cost + self.find_min_cost(left, try_cut, cuts_left, try_cut_index) + self.find_min_cost(try_cut, right, try_cut_index+1, cuts_right)
            if try_cut_cost < min_total_cost:
                min_cut_index = try_cut_index
                min_cut = self.cuts[min_cut_index]
                min_total_cost = try_cut_cost

        self.trace_table[left][right] =  min_cut_index
        self.total_cost_table[left][right] = min_total_cost
        return min_total_cost
    
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        if m == 0:
            return 0
        if m == 1:
            return n
        cuts.sort()
        self.cuts = cuts
        self.n = n
        self.m = m
        
        self.total_cost_table = [[-1 for i in range(n+1)] for i in range(n+1)]
        self.trace_table = [[-1 for i in range(n+1)] for i in range(n+1)]
        cost = n
        # assumming cut with index = 0 is the best cut, lead to mininum total
        min_cut_index = 0
        min_cut = cuts[min_cut_index]
        # caculate the cost using recusive call of minCost, as we will want to
        # solve 2 remainning array
        min_total_cost = cost + self.find_min_cost(0, min_cut, 0, min_cut_index) + self.find_min_cost(min_cut, n, min_cut_index+1, m)
        for try_cut_index in range(m):
            try_cut = cuts[try_cut_index]
            try_total_cost = cost + self.find_min_cost(0, try_cut, 0, try_cut_index) + self.find_min_cost(try_cut, n, try_cut_index+1, m)
            if try_total_cost < min_total_cost:
                min_cut_index = try_cut_index
                min_cut = cuts[min_cut_index]
                min_total_cost = try_total_cost
        print(min_cut_index, min_cut, min_total_cost)
        self.trace_table[0][n] =  min_cut_index
        self.total_cost_table[0][n] =  min_total_cost

        # Check result
        # queue = [(0, n)]
        # while len(queue)>0:
        #     l, r = queue.pop(0) 
        #     m = self.trace_table[l][r]
        #     if m != -1:
        #         print(cuts[m])
        #         if self.trace_table[l][cuts[m]] != -1:
        #             queue.append((l, cuts[m]))
        #         if self.trace_table[cuts[m]][r] != -1:
        #             queue.append((cuts[m],r))
        return min_total_cost

if __name__ == "__main__":
    a = Solution()

    # Input: n = 7, cuts = [1,3,4,5]
    # Output: 16
    result = a.minCost( n = 7, cuts = [1,3,4,5])
    print("test1 is ", result == 16)
    result = a.minCost( n = 9, cuts = [5,6,1,4,2])
    print("test2 is ", result == 22)
    result = a.minCost( n = 10**6, cuts = [i for i in  range (1, 10**6)])
    print("test time limit is ok")
    