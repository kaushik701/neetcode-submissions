class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(start):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for num in range(start, n+1):
                comb.append(num)
                dfs(num+1)
                comb.pop()

        dfs(1)
        return res