class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: time O(n^2) space O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]


        # using hash map => Not Optimal 
        # time O(n^2) & space O(n)
        # track = {}
        # for i in range(len(nums)):
        #     # without checking pre element in dict
        #     track[nums[i]] = target - nums[i]
        #     # ignore the exception cases but this is O(n^2)
        #     j = nums.index(track[nums[i]])
        #     # check the achiving target or not
        #     if (nums[i] + nums[j]) == target:
        #         return [i, j]
        
        # hash map => Optimal Approach
        # time O(n) space O(n)
        track = {}
        for i, val in enumerate(nums):
            
            sub = target - val
            if sub in track:
                return [track[sub], i]
        
            track[val] = i



