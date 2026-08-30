class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort O(nlogn)
        if len(nums) <=1:
            return nums
        
        mid = len(nums) // 2
        # divide and split in middle
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, list1, list2):
        sorted_list = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                sorted_list.append(list1[i])
                i += 1
            else:
                sorted_list.append(list2[j])
                j += 1
        
        # Append whatever is left over
        sorted_list.extend(list1[i:])
        sorted_list.extend(list2[j:])
        
        return sorted_list
        
        # insertation sort O(n^2) : this is not optimised soluntion
        # for i, v in enumerate(nums):
        #     current = v
        #     j = i - 1
        #     while j>=0 and nums[j] > current:
        #         nums[j+1] = nums[j]
        #         j -= 1
        #     nums[j] = current
        # return nums

        




            