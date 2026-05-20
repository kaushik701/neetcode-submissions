from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        have = 0
        needCount = len(need)
        res, reslen = [-1,-1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == needCount:
                if (right-left+1) < reslen:
                    res = [left,right]
                    reslen = right - left + 1
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""