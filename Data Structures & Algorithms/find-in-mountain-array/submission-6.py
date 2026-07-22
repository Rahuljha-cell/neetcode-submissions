class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length-2
        while l <= r:
            m = l + (r-l)//2
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid < right: # left portion ascending
                l = m + 1
            elif left > mid > right: # right
                r = m - 1
            else:
                break
        peak = m
        l, r = 0, peak
        while l <= r: # for left portion (ascending order)
            midl = l + (r-l)//2
            val = mountainArr.get(midl)
            if val < target:
                l = midl + 1
            elif val > target:
                r = midl - 1
            else:
                return midl
        l, r = peak, length-1
        while l <= r: # right portion (decreasing order)
            midr = l + (r-l)//2
            val = mountainArr.get(midr)
            if val < target:
                r = midr - 1
            elif val > target:
                l = midr + 1
            else:
                return midr
        return -1

