class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        for n in nums:
            hashmap[n] += 1
        for key, val in hashmap.items():
            if val > len(nums) // 3:
                res.append(key)
        return res
        