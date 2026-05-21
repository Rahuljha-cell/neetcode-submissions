class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(left, right):
            if (left > right):
                return 
            pivot = nums[(left + right)//2]
            i = left
            j = right
            while (i <= j):
                while (nums[i] < pivot):
                    i += 1
                while (nums[j] > pivot):
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            quicksort(left, j)
            quicksort(i, right)
        quicksort(0, len(nums) - 1)
        return nums