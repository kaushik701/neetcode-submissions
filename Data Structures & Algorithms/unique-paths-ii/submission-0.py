class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # first row
        for c in range(1,n):
            if obstacleGrid[0][c] == 1: dp[0][c] = 0
            else: dp[0][c] = dp[0][c-1]

        # first col
        for r in range(1,m):
            if obstacleGrid[r][0] == 1: dp[r][0] = 0
            else: dp[r][0] = dp[r-1][0]

        # fill rest of grid
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]