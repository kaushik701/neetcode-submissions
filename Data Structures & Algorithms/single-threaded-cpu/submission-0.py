class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [
            [enqueue, process, i] for i, (enqueue, process) in enumerate(tasks)
        ]

        indexed_tasks.sort(key=lambda x: x[0])
        n = len(indexed_tasks)
        res = []

        minHeap = []
        time = 0
        i = 0
        while i < n or minHeap:
            if not minHeap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(minHeap, (process, idx))
                i += 1
        
            process, idx = heapq.heappop(minHeap)
            res.append(idx)
            time += process
        return res
    