class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 0: return 0
        if len(arr) == 1: return 1

        up = 1
        down = 1
        ans = 1

        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                up = down + 1
                down = 1
            elif arr[i-1] > arr[i]:
                down = up + 1
                up = 1
            else: up = down = 1
            ans = max(ans,up,down)
        return ans