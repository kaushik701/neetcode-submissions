"""
Definition of Interval:"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start)
        minHeap = []

        for interval in intervals:
            start,end = interval.start, interval.end
            if minHeap and start >= minHeap[0]: heapq.heappop(minHeap)
            heapq.heappush(minHeap,end)

        return len(minHeap)