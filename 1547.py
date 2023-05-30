import random
from typing import List


class Solution:
    def find_min_cost(self, left, right, cuts_left, cuts_right):
        if (left,right) in self.total_cost_table:
            return self.total_cost_table[(left, right)]
        
        if len(self.cuts[cuts_left: cuts_right]) == 0:
            self.total_cost_table[(left, right)] = 0
            return 0
        
        if len(self.cuts[cuts_left: cuts_right]) == 1:
            self.trace_table[(left, right)] =  cuts_left
            self.total_cost_table[(left, right)] = right - left
            return right - left
        
        cost = right - left
        min_cut_index = cuts_left
        min_cut = self.cuts[min_cut_index]
        min_total_cost = cost \
            + self.find_min_cost(left, min_cut, cuts_left, min_cut_index) \
            + self.find_min_cost(min_cut, right, min_cut_index+1, cuts_right)
        
        # caculate the cost using recusive call of minCost, as we will want to
        # solve 2 remainning array
        for try_cut_index in range(cuts_left +1, cuts_right):
            try_cut = self.cuts[try_cut_index]
            try_cut_cost = cost \
                + self.find_min_cost(left, try_cut, cuts_left, try_cut_index) \
                + self.find_min_cost(try_cut, right, try_cut_index+1, cuts_right)
            if try_cut_cost < min_total_cost:
                min_cut_index = try_cut_index
                min_cut = self.cuts[min_cut_index]
                min_total_cost = try_cut_cost

        self.trace_table[(left, right)] =  min_cut_index
        self.total_cost_table[(left, right)] = min_total_cost
        return min_total_cost
    
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts.sort()
        self.cuts = cuts
        self.total_cost_table = {}
        self.trace_table = {}
        min_total_cost = self.find_min_cost(0, n, 0, m)

        # Backtrace the result for cutting path
        result_cut = []
        queue = [(0, n)]
        while len(queue)>0:
            l, r = queue.pop(0) 
            m = self.trace_table[(l,r)]
            result_cut.append(cuts[m])
            if (cuts[m],r) in self.trace_table:
                queue.append((cuts[m],r))
            if (l, cuts[m]) in self.trace_table:
                queue.append((l, cuts[m]))
        print(result_cut)

        return min_total_cost

if __name__ == "__main__":
    a = Solution()

    # Input: n = 7, cuts = [1,3,4,5]
    # Output: 16
    result = a.minCost( n = 7, cuts = [1,3,4,5])
    print("test 1 is ", result == 16)
    result = a.minCost( n = 9, cuts = [5,6,1,4,2])
    print("test 2 is ", result == 22)
    result = a.minCost( n = 10, cuts = [7,8,9,2,1])
    print("test 3 is ", result == 24)

    result = a.minCost( n = 10**6, cuts = [random.randint(1,10**6-1) for i in  range (1, min(10**6-1, 100))])
    print("test time limit is ok")
    