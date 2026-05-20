class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(nums,target,l,r):
            l,r = 0,len(nums)-1
            while l <= r:
                m = (l+r) // 2
                potentialMatch = nums[m]
                if target == potentialMatch:
                    return m
                elif target < potentialMatch:
                    r = m-1
                else:
                    l = m+1
            return -1 
        return helper(nums,target,0,len(nums)-1)