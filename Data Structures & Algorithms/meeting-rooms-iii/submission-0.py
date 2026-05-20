class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        available = [i for i in range(n)]
        heapq.heapify(available)

        busy = []
        count = [0] * n
        for start,end in meetings:
            duration = end - start

            while busy and busy[0][0] <= start:
                free_end,room = heapq.heappop(busy)
                heapq.heappush(available,room)
            
            if available:
                room = heapq.heappop(available)
                new_end = end
            else:
                free_end, room = heapq.heappop(busy)
                new_end = free_end + duration
            heapq.heappush(busy,(new_end,room))
            count[room] += 1
        max_meetings = max(count)
        for room in range(n):
            if count[room] == max_meetings: return room