class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n
        self.components = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,a,b):
        pa,pb = self.find(a), self.find(b)
        if pa == pb: return False
        if self.rank[pa] < self.rank[pb]: pa,pb = pb,pa
        self.parent[pb] = pa
        self.rank[pa] += self.rank[pb]
        self.components -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges): e.append(i)
        edges.sort(key=lambda e: e[2])

        def kruskal(skip_idx = -1, force_edge=None):
            uf = UnionFind(n)
            total = 0

            if force_edge is not None:
                u,v,w,_ = force_edge
                if uf.union(u,v): total += w
            
            for u,v,w,idx in edges:
                if idx == skip_idx: continue
                if uf.union(u,v): total += w

            if uf.components != 1: return float("inf")
            return total

        base_weight = kruskal()
        critical = []
        pseudo = []

        for u,v,w,idx in edges:
            if kruskal(skip_idx=idx) > base_weight: critical.append(idx)
            else:
                if kruskal(force_edge=[u,v,w,idx]) == base_weight: pseudo.append(idx)
        return [critical,pseudo]
        