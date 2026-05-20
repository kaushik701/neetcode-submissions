class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n =len(s)

        maxFreq = max(freq.values())
        if maxFreq > (n+1) // 2: return ""

        maxHeap = []
        for ch, count in freq.items(): heapq.heappush(maxHeap,(-count, ch))

        res = []
        while len(maxHeap) > 1:
            cnt1, ch1 = heapq.heappop(maxHeap)
            cnt2, ch2 = heapq.heappop(maxHeap)

            res.append(ch1)
            res.append(ch2)

            cnt1 += 1
            cnt2 += 1

            if cnt1 < 0: heapq.heappush(maxHeap, (cnt1,ch1))
            if cnt2 < 0: heapq.heappush(maxHeap, (cnt2,ch2))

        if maxHeap:
            cnt, ch = heapq.heappop(maxHeap)
            res.append(ch)
        
        return "".join(res)