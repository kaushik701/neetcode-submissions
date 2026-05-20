class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        balloons = [1] + nums + [1]

        dp = [[0]*(n+2) for _ in range(n+2)]

        for left in range(n-1,-1,-1):
            for right in range(left+2,n+2):
                for k in range(left+1,right):
                    coins = (
                        dp[left][k] + dp[k][right] + balloons[left] * balloons[k] * balloons[right]
                    )
                    dp[left][right] = max(dp[left][right],coins)
        return dp[0][n+1]