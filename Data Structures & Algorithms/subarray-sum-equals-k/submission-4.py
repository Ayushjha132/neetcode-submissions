class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time O(n) & space O(n)
        # check_dict = defaultdict(int)
        # result = 0
        # sum = 0
        # check_dict[0] = 1
        # for v in nums:
        #     sum += v
        #     prefix_check = sum - k
        #     if prefix_check in check_dict:
        #         result += check_dict[prefix_check]
        #     check_dict[sum] += 1
        # return result


        res = 0
        cunSum = 0
        prefixSum = {0:1}
        for v in nums:
            cunSum += v
            diff = cunSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[cunSum] = 1 + prefixSum.get(cunSum, 0)
        return res

        # naive approch - O(n2) => not optimal 
        # res = 0
        # n = len(nums)
        # for i in range(n):
        #     current_sum = 0
        #     for j in range(i, n):
        #         current_sum += nums[j]
        #         if current_sum == k:
        #             res += 1

        # return res