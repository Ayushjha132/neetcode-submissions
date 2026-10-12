class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count_dict = []

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            
            area = 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur_count = dfs(r, c)
                    count_dict.append(cur_count)

        return max(count_dict) if count_dict else 0