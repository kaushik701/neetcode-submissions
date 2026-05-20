class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q,i) for i,q in enumerate(queries))
        res = [-1] * len(queries)
        min_heap = []
        i = 0

        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start,end = intervals[i]
                length = end-start+1
                heapq.heappush(min_heap,(length,end))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap: res[idx] = min_heap[0][0]
        return res