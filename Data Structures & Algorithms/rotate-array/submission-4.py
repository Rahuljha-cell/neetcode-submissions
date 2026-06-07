class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                count += 1
                current = next_idx
                if start == current:
                    break
            start += 1