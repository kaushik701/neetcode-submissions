class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l,r = 0,len(matrix[0])
        t,b = 0,len(matrix)

        while l < r and t < b:
            for i in range(l,r): #traverse from left to right
                res.append(matrix[t][i])
            t += 1

            for i in range(t,b): # traverse down
                res.append(matrix[i][r-1])
            r -= 1
            if not (l < r and t < b): break

            for i in range(r-1,l-1,-1): #traverse from right to left
                res.append(matrix[b-1][i])
            b -= 1

            for i in range(b-1,t-1,-1): # traverse up
                res.append(matrix[i][l])
            l += 1
        return res