class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def rob_linear(arr):
            prev2 = 0 #dp[i-2]
            prev1 = 0 #dp[i-1]

            for val in arr:
                cur = max(prev1, prev2+val)
                prev2 = prev1
                prev1 = cur
            return prev1

        case1 = rob_linear(nums[:-1]) # exclude last house
        case2 = rob_linear(nums[1:]) # exclude first house
        return max(case1,case2)
