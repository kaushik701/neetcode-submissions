class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(l,r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        
        def dfs(start):
            if start == len(s):
                res.append(path.copy()); return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end+1])
                    dfs(end+1)
                    path.pop()
        dfs(0)
        return res