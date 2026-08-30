class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # brute force approach => note: sometime it is not acceptable on leetcode. 
        # dp = {}

        # def dfs(i,k):
        #     if k == 1: return sum(nums[i:])
        #     if (i, k) in dp: return dp[(i,k)]

        #     res, curSum = float('inf'), 0
        #     for j in range(i, len(nums) - k+1):
        #         curSum += nums[j]
        #         maxSum = max(curSum, dfs(j+1, k-1))
        #         res = min(res, maxSum)
        #         if curSum > res:
        #             break
        #     dp[(i, k)] = res
        #     return res

        # return dfs(0, k)


        # crakhead approach - optimal
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= k
        
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r-l)//2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res