class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            #Duplicate is there:
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]: #left sorted
                if target >= nums[l] and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid-1
        return False

        