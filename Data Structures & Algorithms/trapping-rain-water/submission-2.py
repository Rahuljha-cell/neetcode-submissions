class Solution:
    def trap(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        if not height:
            return 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
        return res