import heapq 
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if q and q[0][1] == time: 
                heapq.heappush(maxHeap, q.popleft()[0])
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1

                if cnt != 0:
                    q.append([cnt, time+n+1])
        return time