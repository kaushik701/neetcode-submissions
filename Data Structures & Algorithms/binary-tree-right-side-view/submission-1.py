# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        """
        # recursive dfs solution
        def dfs(node,depth):
            if not node: return
            if depth == len(res): res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root,0)
        return res
        """

        # BFS solution
        if not root: return res
        queue = deque([root])
        while queue:
            level_size = len(queue)
            rightmost_val = None
            for _ in range(level_size):
                node = queue.popleft()
                rightmost_val = node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(rightmost_val)
        return res