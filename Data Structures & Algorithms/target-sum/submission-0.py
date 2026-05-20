class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or (total+target) % 2 == 1: return 0
    
        S = (total+target) // 2
        dp = [0] * (S+1)
        dp[0] = 1

        for num in nums:
            for s in range(S, num-1,-1):
                dp[s] += dp[s-num]
        return dp[S]