class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))

        best = [[float("inf")] * (k+2) for _ in range(n)]
        best[src][0] = 0

        heap = [(0,src,0)]

        while heap:
            cost,city,flights_used = heapq.heappop(heap)
            if city == dst: return cost
            if flights_used == k+1: continue
            if cost > best[city][flights_used]: continue

            for nei, price in graph[city]:
                next_cost = cost + price
                next_flights = flights_used + 1

                if next_cost < best[nei][next_flights]:
                    best[nei][next_flights] = next_cost
                    heapq.heappush(heap,(next_cost, nei, next_flights))
        return -1