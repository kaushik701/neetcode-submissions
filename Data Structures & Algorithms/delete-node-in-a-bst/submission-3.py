# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if not root.left: return root.right #case1 : no left child
        if not root.right: return root.left #case2: no right child

        # case 3: both child exist. find inorder successor (smallest node in the right subtree)
        successor = root.right
        while successor.left: successor = successor.left
        root.val = successor.val

        root.right = self.deleteNode(root.right, successor.val)

        return root