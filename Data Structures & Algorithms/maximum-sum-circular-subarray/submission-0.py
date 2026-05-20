class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        curMax = 0
        maxSum = nums[0]

        curMin = 0
        minSum = nums[0]

        for x in nums:
            total += x
            curMax = max(curMax+x,x)
            maxSum = max(maxSum,curMax)

            curMin = min(curMin+x,x)
            minSum = min(minSum,curMin)

        if minSum == total: return maxSum
        return max(maxSum,total-minSum)