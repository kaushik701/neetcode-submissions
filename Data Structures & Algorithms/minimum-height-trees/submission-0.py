class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = [[] for _ in range(n)]
        degree = [0] * n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()
        for i in range(n):
            if degree[i] == 1: q.append(i)
        remaining = []

        while q:
            level_size = len(q)
            remaining = []
            for _ in range(level_size):
                leaf = q.popleft()
                remaining.append(leaf)

                for nei in adj[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1: q.append(nei)
        return remaining