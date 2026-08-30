class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # brute force
        # res = float('inf')
        # n = len(nums)
        # for i in range(n):
        #     curr = 0
        #     for j in range(i, n):
        #         curr += nums[j]
        #         if curr >= target:
        #             res = min(res, j - i + 1)
        #             break

        # return 0 if res == float('inf') else res

        # optimal sol
        n = len(nums)
        l = 0
        curr_sum = 0
        ans = float('inf')

        for r in range(n):
            curr_sum += nums[r]

            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans