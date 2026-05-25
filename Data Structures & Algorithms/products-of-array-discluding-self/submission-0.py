class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        multiply = 1
        zero_count = nums.count(0)
        for i in range(len(nums)):
            if nums[i] != 0:
                multiply *= nums[i]
        for num in nums:
            if zero_count > 1:
                div = 0
            elif zero_count == 1:
                div = multiply if num == 0 else 0
            else:
                div = multiply // num
            output.append(div)
        return output
