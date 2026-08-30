class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # brute force : linear search 

        # optimal : O(logn)
        length = mountainArr.length()

        # find peak
        l, r = 0, length - 2 # both bottom will not be peak (optimsation)
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        # possible in python beacuse context of m is still avalible
        peak = m 

        # search left portion
        l, r = 0, peak
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        # search right portion
        l, r = peak, length - 1
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1


