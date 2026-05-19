class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        for num in nums:
            if num in hashmap:
                hashmap[num] +=1 
            else:
                hashmap[num] = 1
        for num in hashmap:
            if hashmap[num] > n/2: 
                return num
           