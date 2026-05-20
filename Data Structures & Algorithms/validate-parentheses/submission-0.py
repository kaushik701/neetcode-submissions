class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack or stack[-1] != mapping[c]: 
                    return False
                stack.pop()
        return not stack