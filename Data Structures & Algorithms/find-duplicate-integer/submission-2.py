class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force approach 
        # s = set()
        # for i in nums:
        #     if i not in s:
        #         s.add(i)
        #     else:
        #         return i

        # optimal sol using floyd's fast and slow
        # memorize the solution - no option difficult to explain 

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
