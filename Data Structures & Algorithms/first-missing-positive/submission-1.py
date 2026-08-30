class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # navie approch time: O(nlogn) space: O(1)
        s = sorted(set(nums)) # remove dublicates and sorted  
        target = 1 # minium possible +ve number 
        for num in s:
            if num > 0:
                if num == target:
                    target += 1
                elif num > target:
                    return target
        return target 

        # optimal way time: O(n) space: O(1)

