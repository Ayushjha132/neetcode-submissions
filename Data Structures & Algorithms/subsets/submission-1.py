class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        
        def dfs(i):
            res.append(sol.copy()) # Every state is a valid subset
            
            for j in range(i, len(nums)):
                sol.append(nums[j])
                dfs(j + 1)
                sol.pop() # Backtrack
                
        dfs(0)
        return res