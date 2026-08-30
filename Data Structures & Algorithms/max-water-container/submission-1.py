class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        '''
        max_arr = 0
        n = len(heights)
        for i in range(n):
            for j in range(i+1, n):
                # area = min height among two * distance
                arr = (j-i) * min(heights[i],heights[j])
                if max_arr < arr:
                    max_arr = arr
        return max_arr 
        '''

        # optimal 
        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            distance = r-l # distance
            min_height = min(heights[l], heights[r]) # min height
            area = distance * min_height
            max_area = max(area, max_area)
            
            # move the height of smaller height side
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
            