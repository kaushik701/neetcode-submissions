class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        jump_count = 0
        curr_jump_end = 0
        farthest_reachable = 0

        for i in range(len(nums)-1):
            farthest_reachable = max(farthest_reachable,i+nums[i])
            if i == curr_jump_end:
                jump_count += 1
                curr_jump_end = farthest_reachable
        return jump_count