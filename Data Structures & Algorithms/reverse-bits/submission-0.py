class Solution:
    def reverseBits(self, n: int) -> int:
        stack = ""
        for _ in range(32):
            stack += str(n & 1)
            n >>= 1
        return int(stack,2)