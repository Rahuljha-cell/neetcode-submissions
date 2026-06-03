class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_cpy = nums1[:m]
        idx = 0 #idx for nums1
        i = j = 0 # i for nums1_cpy and j for nums2
        while idx < m+n:
            if j >= n or (i < m and nums1_cpy[i] <= nums2[j]):
                nums1[idx] = nums1_cpy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j+=1
            idx += 1
        

        