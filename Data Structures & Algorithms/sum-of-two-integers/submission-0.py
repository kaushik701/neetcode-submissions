class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF      # keep numbers within 32 bits
        max_int = 0x7FFFFFFF   # largest positive 32-bit signed int
        while b != 0:
            carry = (a & b) << 1
            a = (a^b) & mask
            b = carry & mask
        if a <= max_int: return a
        return ~((a^mask))