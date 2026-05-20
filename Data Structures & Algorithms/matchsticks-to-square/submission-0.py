class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        side_len, rem = divmod(total, 4)
        if rem != 0: return False
        if not matchsticks: return False

        if max(matchsticks)> side_len: return False
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks): return sides[0] == sides[1] == sides[2] == sides[3] == side_len
            for k in range(4):
                if sides[k] + matchsticks[i] > side_len: continue
                if k > 0 and sides[k] == sides[k-1]: continue
                sides[k] += matchsticks[i]

                if backtrack(i+1): return True

                sides[k] -= matchsticks[i]
            return False
        return backtrack(0)