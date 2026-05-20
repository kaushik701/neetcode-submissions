class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][1]
        removals = 0

        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start >= prevEnd: prevEnd = end
            else:
                removals += 1
                prevEnd = min(prevEnd, end)
        return removals