class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(A) > len(B): A,B = B,A
        m,n = len(A), len(B)
        total = m+n
        half = total // 2
        l,r = 0,m

        while l <= r:
            i = (l+r) // 2
            j = half-i

            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return float(min(Aright, Bright))

                left_max = max(Aleft,Bleft)
                right_min = min(Aright, Bright)
                return (left_max + right_min) / 2
            
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1