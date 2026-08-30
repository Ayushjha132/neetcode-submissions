class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force method 
        # time O(n^2) and space O(1)

        # while val in nums:
        #     nums.remove(val)
        # return len(nums)


        # two pointers 
        # time O(n) and space O
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k


