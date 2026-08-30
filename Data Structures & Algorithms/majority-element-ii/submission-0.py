class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        data = []
        for k, v in count.items():
            if v > len(nums) // 3:
                data.append(k)

        return data