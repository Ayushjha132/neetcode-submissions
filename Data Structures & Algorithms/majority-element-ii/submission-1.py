class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # hash map approach but time O(n) space O(n)
        # count = {}
        # for i in range(len(nums)):
        #     if nums[i] not in count:
        #         count[nums[i]] = 1
        #     else:
        #         count[nums[i]] += 1
        # data = []
        # for k, v in count.items():
        #     if v > len(nums) // 3:
        #         data.append(k)
        # return data
        
        # Extended Boyer-Moore Voting - time O(n) and space O(1)

        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
