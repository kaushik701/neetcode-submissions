class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self,word,i):
        curr = self
        curr.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.refs += 1
        curr.idx = i 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i],i)
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def getIndex(c): return ord(c) - ord('a')

        def dfs(r,c,node):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "*" 
            or not node.children[getIndex(board[r][c])]): return

            tmp = board[r][c]
            idx = getIndex(tmp)
            prev = node
            node = node.children[idx]

            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1

                if node.refs == 0:
                    prev.children[idx] = None
                    node = None
                    return
            
            board[r][c] = "*"

            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)

            board[r][c] = tmp
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        return res