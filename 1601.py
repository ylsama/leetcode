from typing import List
from ulti.testHelper.testHelper import TestHelper


class Solution:
    def bit_1_pos(self, number):
        for pos, c in enumerate(bin(number)[2:][::-1]):
            if c == '1':
                yield pos

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        current_max = 0
        
        for request_served in range(1 << requests.__len__()):
            building = [0] * n
            pos = requests.__len__() - 1
            if request_served.bit_count() <= current_max:
                continue
                
            for pos in self.bit_1_pos(request_served):
                building[requests[pos][0]] -= 1
                building[requests[pos][1]] += 1
				
            check = True
            for i in range(n):
                if building[i] != 0:
                    check = False
                    break
                    
            if check:
                current_max = request_served.bit_count()

        return current_max


def test():
    test = TestHelper()
    a = Solution()
    test.quickTest(a.maximumRequests, [3, [[0,0],[1,2],[2,1]]], 3)
    test.quickTest(a.maximumRequests, [4, [[0,3],[3,1],[1,2],[2,0]]], 4)


if __name__ == "__main__":
    test()