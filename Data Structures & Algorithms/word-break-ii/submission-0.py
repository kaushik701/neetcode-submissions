class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo  = {}

        def dfs(start):
            if start in memo: return memo[start]
            if start == len(s): return [""]
            res = []

            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in wordSet:
                    suffix_sentences = dfs(end)
                    for sentence in suffix_sentences:
                        if sentence == "": res.append(word)
                        else: res.append(word + " " + sentence)
            memo[start] = res
            return res
        
        return dfs(0)