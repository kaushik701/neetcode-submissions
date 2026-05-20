class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0: return 0
            area = 1
            grid[r][c] = 0

            area += dfs(r+1,c) # down
            area += dfs(r-1,c) # up
            area += dfs(r,c+1) # right
            area += dfs(r,c-1) # left

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c)) 
        return maxArea