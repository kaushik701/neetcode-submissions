class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            indegree = [0] * (k+1)
            adj = [[] for _ in range(k+1)]

            for u,v in edges:
                adj[u].append(v)
                indegree[v] += 1

            order = []
            q = deque()

            for i in range(1,k+1):
                if indegree[i] == 0: q.append(i)

            while q:
                node = q.popleft()
                order.append(node)

                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0: q.append(nei)
            return order

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if len(row_order) != k: return []
        if len(col_order) != k: return []

        res = [[0] * k for _ in range(k)]
        colIndex = [0] * (k+1)
        for col in range(k):
            colIndex[col_order[col]] = col

        for row in range(k):
            val = row_order[row]
            c = colIndex[val]
            res[row][c] = val
        
        return res