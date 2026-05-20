from typing import List
import math

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] = max score diff current player can achieve from i
        dp = [0] * (n + 1)  # dp[n] = 0 by default
        # For convenience, fill dp[0..n-1] with -inf first
        for i in range(n):
            dp[i] = -math.inf

        # Fill from right to left
        for i in range(n - 1, -1, -1):
            total = 0
            # try taking 1, 2, or 3 stones
            for k in range(3):
                if i + k >= n:
                    break
                total += stoneValue[i + k]
                dp[i] = max(dp[i], total - dp[i + k + 1])

        alice_diff = dp[0]

        if alice_diff == 0:
            return "Tie"
        elif alice_diff > 0:
            return "Alice"
        else:
            return "Bob"