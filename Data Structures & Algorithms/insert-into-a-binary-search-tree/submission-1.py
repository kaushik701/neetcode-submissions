# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        # recursive solution
        if not root: return TreeNode(val)
        if val < root.val: root.left = self.insertIntoBST(root.left,val)
        else: root.right = self.insertIntoBST(root.right,val)
        return root
        """
        # iterative solution
        if not root: return TreeNode(val)
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
