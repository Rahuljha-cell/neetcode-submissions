class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        deq = deque()
        result = []
        if n == 0:
            return []
        for i in range(n):
            while deq and deq[0] <= i-k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            if i >= k-1:
                result.append(nums[deq[0]])
        return result

        