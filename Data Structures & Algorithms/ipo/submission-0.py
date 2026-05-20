class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        minCapital = []
        for i in range(n): heapq.heappush(minCapital, (capital[i], profits[i]))
        maxProfit = []
        curr_capital = w
        for _ in range(k):
            while minCapital and minCapital[0][0] <= curr_capital:
                cap_req, prof = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -prof)

            if not maxProfit: break

            bestProfit = -heapq.heappop(maxProfit)
            curr_capital += bestProfit
        
        return curr_capital