class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        bit = 1
        while n > 0:
            if (x & bit) == 0:
                if n & 1: ans |= bit
                n >>= 1
            bit <<= 1
        return ans