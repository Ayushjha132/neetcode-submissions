class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # most optimal and mathematical appraoch is here 
        res = 0
        for n in nums:
            # uing bitwise OR 
            res = res | n
            
        return res * 2**(len(nums)-1) 
