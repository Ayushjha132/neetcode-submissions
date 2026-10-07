class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    total += 4
                    # remove of sides count for shared one
                    if r + 1 < ROWS and grid[r+1][c] == 1:
                        total -= 1
                    if r - 1 >= 0 and grid[r-1][c] == 1:
                        total -= 1
                    if c + 1 < COLS and grid[r][c+1] == 1:
                        total -= 1
                    if c - 1 >= 0 and grid[r][c-1] == 1:
                        total -= 1
        return total