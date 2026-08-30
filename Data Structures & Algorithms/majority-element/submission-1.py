class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time O(n) and space O(n)
        count = {}
        result = 0
        max_val = 0
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            if count[n] > max_val:
                result = n
                max_val = count[n]
        return result
        
        
        