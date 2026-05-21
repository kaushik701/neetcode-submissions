class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        expected = len(nums) * (len(nums)+1) // 2
        actual = sum(nums)
        return expected - actual
        """
        """xorr = 0
        for i in range(len(nums)+1):
            xorr ^= i
        for num in nums: xorr ^= num
        return xorr
        """
        res = len(nums)
        for i in range(len(nums)):
            res += (i-nums[i])
        return res