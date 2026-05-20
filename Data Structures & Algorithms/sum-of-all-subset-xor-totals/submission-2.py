class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        def dfs(i, currXor):

            nonlocal total
            if i == n:
                total += currXor
                return
            
            dfs(i+1, currXor)
            dfs(i+1, currXor^nums[i])
        
        dfs(0,0)
        return total