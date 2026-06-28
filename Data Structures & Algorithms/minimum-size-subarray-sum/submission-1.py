class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum >= target:
                    res = min(res, j-i+1)
                    break
        return 0 if res == float('inf') else res