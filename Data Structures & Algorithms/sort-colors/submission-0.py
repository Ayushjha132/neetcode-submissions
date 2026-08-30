class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force O(n^2) => bubble sort
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         if nums[i] > nums[j]:
        #             tem = nums[j]
        #             nums[j] = nums[i]
        #             nums[i] = tem
        
        # optimal way => O(n)
        # as here all elements belong to a one of the fixed three groups only

        count0 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if num == 0: count0 += 1
            elif num == 1: count1 += 1
            elif num == 2: count2 += 1
        
        for i in range(count0):
            nums[i] = 0
        
        for i in range(count0, count0+count1):
            nums[i] = 1
        
        for i in range(count0+count1, len(nums)):
            nums[i] = 2
        

