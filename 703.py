from queue import PriorityQueue
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = PriorityQueue()
        self.before_nums = PriorityQueue()
        
        for i in nums:
            self.before_nums.put(-i)
            if self.nums.qsize() == k:
                self.before_nums.put(-self.nums.get())
            self.nums.put(-self.before_nums.get())
        
    def add(self, val: int) -> int:
        self.before_nums.put(-val)
        if self.nums.qsize() == self.k:
            self.before_nums.put(-self.nums.get())
        self.nums.put(-self.before_nums.get())
        return self.nums.queue[0]



if __name__=="__main__":
    request = [[1,[]],[-3],[-2],[-4],[0],[4]]
    result = KthLargest(request[0][0], request[0][1])
    for i in range(1, len(request)):
        print(result.add(request[i][0]))
