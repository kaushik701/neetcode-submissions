class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False]*len(s) # dp[i] = True if index i is reachable
        dp[0] = True
        # count of reachable indices in the current window [i - maxJump, i - minJump]
        cnt = 0
        for i in range(1,len(s)):
            enter = i-minJump # when i - minJump enters the window, add its dp value
            if enter >= 0 and dp[enter]: cnt += 1
            leave = i-maxJump-1 # when i - maxJump - 1 leaves the window, subtract its dp value
            if leave >= 0 and dp[leave]: cnt -= 1

            # index i is reachable if there's at least one reachable index in the window
            # and s[i] is '0' (we can only land on zeroes)
            if s[i] == '0' and cnt > 0: dp[i] = True
        return dp[len(s)-1]