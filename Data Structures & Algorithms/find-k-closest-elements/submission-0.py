class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # two pointer approach 
        l, r = 0 , len(arr) - k
        while l < r:
            m = (l+r) // 2
            # mathematical logic is here
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]

        # lambda approach 
        # sort by difference and them filter k and sort back in asc
        # arr.sort(key=lambda num: (abs(num - x), num))
        # return sorted(arr[:k])

    