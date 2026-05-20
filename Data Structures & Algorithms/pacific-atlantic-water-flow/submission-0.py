class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)] # [down,up,right,left]

        def dfs(r,c,visited):
            if (r,c) in visited: return
            visited.add((r,c))

            for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0 <=nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] >= heights[r][c]: dfs(nr,nc, visited)
        for c in range(cols):
            dfs(0,c,pacific) #top edge
            dfs(rows-1,c,atlantic) #bottom edge
        for r in range(rows):
            dfs(r,0,pacific) #left edge
            dfs(r,cols-1,atlantic) #right edge
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic: res.append([r,c])
        
        return res
            