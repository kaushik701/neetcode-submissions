class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for (a,b), val in zip(equations, values):
            adj[a].append((b,val)) # a/b
            adj[b].append((a,1.0/val)) # b/a

        def dfs(src, dst, visited):
            if src not in adj or dst not in adj: return -1.0
            if src == dst: return 1.0
            visited.add(src)

            for nei, w in adj[src]:
                if nei in visited: continue
                res = dfs(nei, dst, visited)
                if res != -1.0:
                    return w*res # src/dst = (src/nei) * (nei/src) = w*res
            return -1.0

        return [dfs(x,y,set()) for x,y in queries]
        