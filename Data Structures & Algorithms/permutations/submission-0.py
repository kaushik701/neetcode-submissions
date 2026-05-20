class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                    dfs()
                    perm.pop()
                    used[i] = False
        dfs()
        return res