class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        check_dict = defaultdict(int)
        result = 0
        sum = 0
        check_dict[0] = 1
        for v in nums:
            sum += v
            prefix_check = sum - k
            if prefix_check in check_dict:
                result += check_dict[prefix_check]
            check_dict[sum] += 1
        return result