class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary: trie.addWord(w)
        dp = [0] * (len(s)+1)
        for i in range(len(s)-1,-1,-1):
            dp[i] = 1 + dp[i+1]

            curr = trie.root
            for j in range(i,len(s)):
                c = s[j]
                if c not in curr.children: break
                curr = curr.children[c]
                if curr.isWord: dp[i] = min(dp[i], dp[j+1])
        return dp[0]