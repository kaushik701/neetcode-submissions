class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    if dp[i]: break
        return dp[0]


        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        max_len = max((len(w) for w in wordDict), default=0)

        for i in range(1, n + 1):
            # Only need to look back at most max_len characters
            for L in range(1, max_len + 1):
                if i - L < 0:
                    break
                if not dp[i - L]:
                    continue
                if s[i - L:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]