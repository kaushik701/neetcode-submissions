class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPalindrome(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] ==s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            res += countPalindrome(i,i) # count odd length string
            res += countPalindrome(i,i+1) # count even length string
        return res
