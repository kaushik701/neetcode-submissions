class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 # farthest index we can reach so far
        for i, jump in enumerate(nums):
            # If current index is beyond what we can reach, we are stuck
            if i > maxReach: return False
            # Update farthest reachable index
            maxReach = max(maxReach,i+jump)
        # If we never got stuck, we can reach the last index
        return True