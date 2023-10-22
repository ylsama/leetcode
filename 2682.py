from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        result = set([i for i in range(n)])
        i = 0
        index = 1
        while (i % n) in result:
            result -= set([i % n])
            i = (k * index + i) % n
            index += 1
            # print (i % n)
        return [i+1 for i in list(result)]


if __name__=="__main__":
    a = Solution()
    result = a.circularGameLosers(n = 4, k = 4)
    print(result, result == [2,3,4])
    result = a.circularGameLosers(n = 5, k = 2)
    print(result, result == [4,5])