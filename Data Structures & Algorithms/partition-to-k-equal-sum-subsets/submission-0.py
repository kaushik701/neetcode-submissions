class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target, rem = divmod(total,k)
        if rem != 0: return False
        if len(nums) < k: return False
        nums.sort(reverse=True)
        
        if nums[0] > target: return False
        bucket_sums = [0]*k

        def backtrack(index):
            if index == len(nums): return True

            for b in range(k):
                if bucket_sums[b] + nums[index] > target: continue
                if b > 0 and bucket_sums[b] == bucket_sums[b-1]: continue

                bucket_sums[b] += nums[index]
                if backtrack(index+1): return True
                bucket_sums[b] -= nums[index]
            return False
        
        return backtrack(0)