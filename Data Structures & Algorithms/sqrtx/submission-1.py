class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        # i = 0
        # while i * i <= x:
        #     i += 1
        # return i - 1

        # optimal way
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-l)//2)
            if m*m < x:
                l = m + 1
                res = m
            elif m*m > x:
                r = m - 1
            else:
                return m
        return res
