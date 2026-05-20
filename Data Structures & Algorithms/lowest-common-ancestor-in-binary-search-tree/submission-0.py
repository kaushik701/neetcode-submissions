# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minVal = min(p.val, q.val)
        maxVal = max(p.val,q.val)

        if not root: return None
        while root:
            if root.val < minVal: root = root.right
            elif root.val > maxVal: root = root.left
            else: return root
        return None
