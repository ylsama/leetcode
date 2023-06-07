"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

"""
This look like a graph problem; quite simmilar to 547. Number of Provinces

We just need some better way to find adjNode
        a node[i] is intervals[i] = [start_i, end_i]
    1. First way is to sort all the interval by start_i
    
    2. If end_i overlap start_(i+1) or end_i > start_(i+1); it mean they adjNodes
    
    3. Here, we can keep try to combine them. Repeat the process untill we find next one isn't overlap. 
"""
from typing import List


class Solution:
    def sortKey(self,item):
        return item[0]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resultIntervals = []
        intervals.sort(key = self.sortKey)
        nodes = intervals
        
        MAX_LOOP = len(nodes)
        index = -1
        for _ in range(MAX_LOOP):
            index += 1
            if index == len(nodes):
                break
                
            start, end = nodes[index]
            
            for nextStart, nextEnd in nodes[index+1:]:
                if end >= nextStart:
                    end = max(end, nextEnd)
                    index += 1
                else:
                    break
            merged = [start, end]
            
            resultIntervals.append(merged)
        return resultIntervals
    
def test():
    a = Solution()
    # Example 1
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = [[1,6],[8,10],[15,18]]
    print("Test 1 is", a.merge(intervals) == result)
    
    
    # Example 2
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = [[1,6],[8,10],[15,18]]
    print("Test 2 is", a.merge(intervals) == result)
    
test()