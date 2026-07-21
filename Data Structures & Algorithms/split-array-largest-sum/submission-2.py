class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        def canSplit(largest):
            subarray, currSum = 0, 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subarray += 1
                    currSum = n
            return subarray+1 <= k
        res = r
        while l <= r:
            mid = (l+r)//2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res