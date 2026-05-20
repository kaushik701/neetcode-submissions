class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2 : return 1
        f,s,t = 0,1,1
        for _ in range(3,n+1): f,s,t = s,t,f+s+t
        return t