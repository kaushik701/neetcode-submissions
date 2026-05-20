class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start,rem):
            if rem == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: continue

                if candidates[i] > rem: break
                path.append(candidates[i])

                dfs(i+1, rem-candidates[i])
                path.pop()

        dfs(0,target)
        return res