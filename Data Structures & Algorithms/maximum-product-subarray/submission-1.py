class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for num in nums[1:]:
            prevMax = curMax
            prevMin = curMin

            curMax = max(num, prevMax * num, prevMin * num)
            curMin = min(num, prevMax * num, prevMin * num)

            res = max(res, curMax)

        return res