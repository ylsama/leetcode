from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Start with a subarray nums[k:k] (inclusive, python is exlusive tho)
        l, r = k, k
        # Init some defaul value
        minElement = nums[k]
        score = nums[k]
        # Loop until all possible nums is add to the subarray
        while (l >= 0 or r < len(nums)):
            # Expanding to the left until `l` is out of array scope, and not changing the minimum value
            while l > 0:
                if nums[l-1] >= minElement:
                    l -= 1
                else:
                    break
            # Doing so with the right too
            while r < len(nums) - 1:
                if nums[r+1] >= minElement:
                    r += 1
                else:
                    break
            # Calulating current score and update the maximum score value
            currScore = minElement * (r - l + 1)
            # Debug line
            print(
                f"minElement = {minElement}; left = {l}; right = {r}; score = {currScore}")
            if score < currScore:
                score = currScore

            # Handle the updating minElement expanding
            # Case 1: No more element to add
            if l == 0 and r == len(nums) - 1:
                break
            # Case 2: Left or Right can't expanding any more (l or r out of scope).
            if l == 0:
                r += 1
                minElement = nums[r]
                continue
            if r == len(nums) - 1:
                l -= 1
                minElement = nums[l]
                continue
            # Case 3: We piority the side where it have the bigger value.
            if nums[l] > nums[r]:
                l -= 1
                minElement = nums[l]
            else:
                r += 1
                minElement = nums[r]

        return score


a = Solution()
nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872]
k = 5
a.maximumScore(nums=nums, k=k)
