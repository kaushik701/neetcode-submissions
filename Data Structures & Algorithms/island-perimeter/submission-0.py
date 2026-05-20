class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0: return 1
            if (i,j) in visit: return 0
            visit.add((i,j))
            perim = 0
            perim += dfs(i,j+1) #right
            perim += dfs(i+1,j) #down
            perim += dfs(i,j-1) #left
            perim += dfs(i-1,j) #up

            return perim
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: return dfs(i,j)
        return 0