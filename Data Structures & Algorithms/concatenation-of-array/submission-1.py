class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums # build in operation
        

        #second method
        #allocate the length of 2n
        n = len(nums)
        ans = [0] * (2 * n)
        # insert nums[i] at ans[i] & ans[i+ n]
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans
    

