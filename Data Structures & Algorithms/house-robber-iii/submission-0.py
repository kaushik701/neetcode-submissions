# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: return (0,0)

            # recursively compute for left and right children
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # if we rob this node, we must skip its children
            rob_curr = node.val + left_skip + right_skip

            skip_curr = max(left_rob, left_skip) + max(right_rob, right_skip)

            return rob_curr, skip_curr
        
        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)