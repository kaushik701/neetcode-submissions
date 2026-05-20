class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row = -1
        top, bot = 0, rows-1
        while top <= bot:
            mid = (top+bot) // 2
            if target > matrix[mid][cols-1]: top = mid+1
            elif target < matrix[mid][0]: bot = mid-1
            else:
                row = mid
                break
        if row == -1: return False

        left, right = 0, cols-1
        while left <= right:
            mid = (left+right) // 2
            val = matrix[row][mid]
            if val == target: return True
            elif val < target: left = mid+1
            else: right = mid-1
        return False