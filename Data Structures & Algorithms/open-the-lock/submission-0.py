class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        dead = set(deadends)

        if start in dead: return -1
        if target == start: return 0

        q = deque()
        q.append((start,0))
        visited = set([start])

        def neighbors(combo):
            res = []
            for i in range(4):
                digit = int(combo[i])
                up = (digit + 1) % 10
                res.append(combo[:i]+str(up)+combo[i+1:])

                down = (digit - 1) % 10
                res.append(combo[:i]+str(down)+combo[i+1:])
            return res
        
        while q:
            combo, steps = q.popleft()
            for nxt in neighbors(combo):
                if nxt in dead or nxt in visited: continue
                if nxt == target: return steps+1
                visited.add(nxt)
                q.append((nxt,steps+1))
        return -1