class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # brute force method using fixed sliding window approach
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, min(n, i+k+1)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        # optimal approach
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
