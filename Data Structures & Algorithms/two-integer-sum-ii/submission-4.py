class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        # l = len(numbers)
        # for i in range(l-1):
        #     num = target - numbers[i]
        #     for j in range(i+1, l):
        #         if num == numbers[j]:
        #             return [i+1, j+1]

        # optimal
        # time O(n) space(1)
        loop = True
        i = 0
        j = len(numbers)-1

        while loop:
            curr_sum = numbers[j] + numbers[i]
            if curr_sum == target:
                loop = False
                return [i+1, j+1]
            elif curr_sum > target:
                j -= 1
            else:
                i += 1

            
