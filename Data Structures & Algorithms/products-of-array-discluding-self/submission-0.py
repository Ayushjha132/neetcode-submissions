class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force method - O(n^2)time and O(n)space
        l = len(nums)
        mul = [0] * l
        for i in range(l):
            m = 1
            for j in range(l):
                if i == j:
                    continue
                m *= nums[j]
            mul[i] = m
        return mul
