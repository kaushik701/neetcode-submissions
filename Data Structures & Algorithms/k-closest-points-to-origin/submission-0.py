import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points: 
            dist_sq = x*x + y*y
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist_sq,x,y))
            else:
                if dist_sq < -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist_sq,x,y))
        
        res = []
        while maxHeap:
            _,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        
        return res
