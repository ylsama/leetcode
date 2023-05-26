from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        maxC = 0
        n = len(status)
        openedBox = []
        stuckedBox = set()
        for i in initialBoxes:
            if status[i] == 1:
                openedBox.append(i)
            else:
                stuckedBox.add(i)
        trace = [True] * n 
        while len(openedBox)>0:
            last = openedBox.pop()
            if (trace[last]):
                for key in keys[last]:
                    status[key] = 1
                    if key in stuckedBox:
                        stuckedBox = stuckedBox - set([key])
                        openedBox += [key]
                for box in containedBoxes[last]:
                    if status[box] == 1:
                        openedBox += [box]
                    else:
                        stuckedBox.add(box)
                maxC += candies[last]
                trace[last] = False
        return maxC
        


if __name__=="__main__":
    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[1],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [0]
    a = Solution()
    result = a.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print(result)
