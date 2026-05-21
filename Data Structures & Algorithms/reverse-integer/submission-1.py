class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        rev = 0
        num = x
        while num != 0:
            digit = int(num % 10)
            if num < 0 and digit > 0: digit -= 10
            num = (num-digit) // 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > INT_MAX % 10): return 0
            if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and digit < INT_MIN % 10): return 0
            rev = rev * 10 + digit
        return rev