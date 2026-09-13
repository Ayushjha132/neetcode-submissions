class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        sol = []

        def dfs(i):
            # Base case: when we reach the end of the array, 
            # add a copy of the current subset to the result
            if i == n:
                res.append(sol[:])
                return 
            
            # Choice 1: Don't include nums[i]
            dfs(i + 1)

            # Choice 2: Include nums[i]
            sol.append(nums[i])
            dfs(i + 1)
            sol.pop() # Backtrack

        dfs(0)
        return res