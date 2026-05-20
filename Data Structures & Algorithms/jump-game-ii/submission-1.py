class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0 # already at the last index
        jump_count = 0 # number of jumps taken
        curr_jump_end = 0 # end of the current jump's range
        farthest_reachable = 0  # farthest index we can reach overall so far

        # We only iterate to n - 1 because we don't need to jump from the last index
        for i in range(len(nums)-1):
            # update farthest index we can reach from positions seen so far
            farthest_reachable = max(farthest_reachable,i+nums[i])
            # if we've reached the end of the current jump range,
            # we must "commit" to a new jump
            if i == curr_jump_end:
                jump_count += 1
                curr_jump_end = farthest_reachable
        return jump_count