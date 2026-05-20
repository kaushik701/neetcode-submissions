class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dist = [[float("inf")] * len(grid) for _ in range(len(grid))]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0],0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            cost,r,c = heapq.heappop(heap)
            if r == len(grid)-1 and c == len(grid)-1: return cost
            if cost > dist[r][c]: continue
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid):
                    new_cost = max(cost,grid[nr][nc])
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(heap,(new_cost,nr,nc))
        return -1 