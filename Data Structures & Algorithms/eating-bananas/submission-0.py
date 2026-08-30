class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # O(n)
        ans = r

        def comEat(speed):
            total_time = 0
            for pile in piles:
                total_time += (pile + speed - 1) // speed
            return total_time

        while l <= r:
            m = l + (r-l)//2 # hour of eating banana
            
            if comEat(m) <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans


