class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # this is not optimal as O(n^2)

        # l = len(nums)
        # for i in range(l):
        #     for j in range(i+1, l):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # hash map approch

        hash_map = {}
        l = len(nums)
        for i in range(l):
            if nums[i] in hash_map:
                return True
            hash_map[nums[i]] = False
        return False

