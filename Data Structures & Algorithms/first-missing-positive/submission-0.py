class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 1
        while ans in s:
            ans += 1
        return ans