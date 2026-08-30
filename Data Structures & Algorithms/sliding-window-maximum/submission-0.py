class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # optimal approach - deque 
        res = []
        q = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from windows
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res


        # brute force - here max() is rescan same elements again and again
        # n = len(nums)
        # res = []
        # r = k
        # for l in range(n-k+1):
        #     max_val = max(nums[l : l+r])
        #     res.append(max_val)
        # return res