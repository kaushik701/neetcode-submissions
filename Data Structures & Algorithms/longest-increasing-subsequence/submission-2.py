import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        if len(nums) == 0: return 0
        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]: LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS) """

        tails = []
        for x in nums:
            # Find the insertion position for x in tails
            i = bisect.bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x

        return len(tails)