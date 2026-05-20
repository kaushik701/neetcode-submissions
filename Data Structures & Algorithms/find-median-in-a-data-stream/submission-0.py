class MedianFinder:

    def __init__(self):
        # min_heap: stores the larger half (smallest at top)
        self.min_heap = []
        # max_heap: stores the smaller half as negative values (largest at top)
        self.max_heap = []

    def addNum(self, num: int) -> None:
         # Step 1: push into max_heap (as negative to simulate max-heap)
        # then immediately move the largest of smaller half into min_heap
        heapq.heappush(self.max_heap, -num)
        largest_small = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest_small)

        # Step 2: rebalance if min_heap is more than 1 larger than max_heap
        if len(self.min_heap) > len(self.max_heap) + 1:
            smallest_large = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_large)

    def findMedian(self) -> float:
        # If both heaps have equal size: average of tops
        if len(self.min_heap) == len(self.max_heap):
            if not self.min_heap:  # no elements at all
                return 0.0  # or raise exception
            return (self.min_heap[0] - self.max_heap[0]) / 2.0

        # If sizes differ, min_heap has one extra element
        return float(self.min_heap[0])
        
        