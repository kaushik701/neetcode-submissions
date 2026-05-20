class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        # dp[i][j] = min edit distance between word1[:i] and word2[:j]
        dp = [[0]*(n+1) for _ in range(m+1)]

        # Base cases: transform prefixes to/from empty string
        for i in range(1,m+1): dp[i][0] = i # delete i chars from word1 to get empty word2

        for j in range(1,n+1): dp[0][j] = j # insert j chars to get word2[:j] from empty word1

        # fill table
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] # Characters match, no new operation needed
                else:
                    delete_cost = dp[i-1][j] # delete word1[i-1]
                    insert_cost = dp[i][j-1] # insert word2[j-1]
                    replace_cost = dp[i-1][j-1] # replace word1[i-1] -> word2[j-1]
                    dp[i][j] = 1 + min(delete_cost, insert_cost, replace_cost)
        return dp[m][n]