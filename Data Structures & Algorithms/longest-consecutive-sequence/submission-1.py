class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))

        # current and longest we have seen
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == (sorted_nums[i-1] + 1):
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
        return max(longest_streak, current_streak)
