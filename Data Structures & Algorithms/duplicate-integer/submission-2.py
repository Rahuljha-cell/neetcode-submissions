class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        list.sort(nums)
        for i in range(1, n):
            if (nums[i-1] == nums[i]):
                return True
        return False
            