class Solution:
    def reverseBits(self, n: int) -> int:
        """
        stack = ""
        for _ in range(32):
            stack += str(n & 1)
            n >>= 1
        return int(stack,2)
        """
        res = 0
        for i in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1
        return res