from functools import lru_cache
from itertools import accumulate
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        dp = {}

        def dfs(alice,i,M):
            if i == len(piles): return 0
            if (alice ,i,M) in dp: return dp[(alice,i,M)]

            res = 0 if alice else float("inf")
            total = 0
            for X in range(1,2*M+1):
                if i+X > len(piles): break
                total += piles[i+X-1]
                if alice: res = max(res,total+dfs(not alice, i+X, max(M,X)))
                else: res = min(res,dfs(not alice, i+X, max(M,X)))
            dp[(alice,i,M)] = res
            return res
        return dfs(True,0,1)
        """
        n = len(piles)

        # prefix_sum[i] = sum of piles[0..i-1]
        prefix_sum = list(accumulate(piles, initial=0))

        def total_remaining(i: int) -> int:
            # sum of piles[i..n-1]
            return prefix_sum[n] - prefix_sum[i]

        @lru_cache(None)
        def dfs(i: int, M: int) -> int:
            # maximum stones current player can get starting at index i with parameter M

            # if we can take all remaining piles, take them all
            if 2 * M >= n - i:
                return total_remaining(i)

            best = 0
            # try taking X piles, for 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                opponent = dfs(i + X, max(M, X))
                current = total_remaining(i) - opponent
                best = max(best, current)

            return best

        # Alice starts at index 0 with M = 1
        return dfs(0, 1)