class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        heap = [(0,0)]
        seen = set()

        while len(seen) < len(points):
            cost,i = heapq.heappop(heap)
            if i in seen: continue

            seen.add(i)
            total_cost += cost

            x1,y1 = points[i]
            for j in range(len(points)):
                if j not in seen:
                    x2,y2 = points[j]
                    dist= abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(heap, (dist,j))
        return total_cost