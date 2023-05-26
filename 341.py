from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in frequency.keys():
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
        sortedFrequency = []
        for i in frequency.keys():
            sortedFrequency.append([frequency[i], i])
        sortedFrequency.sort()
        print(sortedFrequency)
        return [i[1] for i in sortedFrequency[-k:]]


if __name__=="__main__":
    a = Solution()
    result = a.topKFrequent(nums = [3,3,3,2,2,1,5,5,5], k = 2)
    print(result)
