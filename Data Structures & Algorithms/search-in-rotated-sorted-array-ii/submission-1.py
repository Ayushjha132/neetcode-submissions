class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2

            if nums[m]==target:
                return True

            # Handle duplicates where we can't tell which side is sorted
            if nums[l] == nums[m] and nums[m] == nums[r]:
                l += 1
                r -= 1
            # right part of array
            elif nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m - 1
            # left part of array
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return False