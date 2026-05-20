class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(largest):
            sub_arrays = 1
            cur_sum = 0
            for n in nums:
                cur_sum += n
                if cur_sum > largest:
                    sub_arrays += 1
                    cur_sum = n
            return sub_arrays <= k
        
        l,r = max(nums), sum(nums)
        ans = r
        while l <= r:
            mid = l+(r-l) // 2
            if canSplit(mid):
                ans = mid
                r = mid-1
            else: 
                l = mid+1
        return ans