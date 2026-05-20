class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n: 
                solution = ["".join(row) for row in board] 
                res.append(solution) 
                return

            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag: continue
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return res
