class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False]*len(s)
        dp[0] = True

        cnt = 0
        for i in range(1,len(s)):
            enter = i-minJump
            if enter >= 0 and dp[enter]: cnt += 1
            leave = i-maxJump-1
            if leave >= 0 and dp[leave]: cnt -= 1

            if s[i] == '0' and cnt > 0: dp[i] = True
        return dp[len(s)-1]