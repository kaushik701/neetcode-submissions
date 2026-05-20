class Solution:
    def tribonacci(self, n: int) -> int:
        f,s,t = 0,1,1
        for _ in range(n): f,s,t = s,t,f+s+t
        return f