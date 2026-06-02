class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - len(nums2)
        j = 0
        while i < len(nums1) and j < len(nums2):
            nums1[i] = nums2[j]
            i +=1
            j+=1
        return nums1.sort()