class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force method - O(n^2)time and O(n)space
        # l = len(nums)
        # mul = [0] * l
        # for i in range(l):
        #     m = 1
        #     for j in range(l):
        #         if i == j:
        #             continue
        #         m *= nums[j]
        #     mul[i] = m
        # return mul

        # better approch - prefix & suffix - O(n)time and O(1)space
        l = len(nums)
        output = [1] * l

        left_mul = 1
        for i in range(l):
            output[i] = left_mul
            left_mul *= nums[i]

        right_mul = 1
        for j in range(l-1, -1, -1):
            output[j] *= right_mul
            right_mul *= nums[j]
            
        return output



