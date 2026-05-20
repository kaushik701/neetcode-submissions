class Solution:
    def isHappy(self, n: int) -> bool: #written in notebook
        visited = set()
        def sumOfsquares(x):
            total = 0
            while x > 0:
                digit = x%10
                total += digit ** 2
                x //= 10
            return total
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = sumOfsquares(n)
        return False