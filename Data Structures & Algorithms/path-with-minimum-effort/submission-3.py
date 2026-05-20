class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def canReach(limit):
            stack = [(0,0)]
            visited = set([(0,0)])

            while stack:
                r,c = stack.pop()
                if r == ROWS-1 and c == COLS-1: return True

                for dr, dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited:
                        diff = abs(heights[nr][nc] - heights[r][c])
                        if diff <= limit:
                            visited.add((nr,nc))
                            stack.append((nr,nc))
            return False

        l,r = 0, 10**6
        ans = r
        while l <= r:
            mid = (l+r) // 2
            if canReach(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans