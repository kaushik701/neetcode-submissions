"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(size,r,c):
            if size == 1: return Node(grid[r][c] == 1, True)
            mid  = size // 2

            topLeft = dfs(mid,r,c)
            topRight = dfs(mid,r,c+mid)
            bottomLeft = dfs(mid,r+mid,c)
            bottomRight = dfs(mid,r+mid,c+mid)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and 
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)
            
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(n,0,0)