class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)
        n =len(s)

        # If any character is too frequent, it's impossible
        maxFreq = max(freq.values())
        if maxFreq > (n+1) // 2: return ""

        # Build a max-heap of (-count, char)
        maxHeap = []
        for ch, count in freq.items(): heapq.heappush(maxHeap,(-count, ch))

        res = []

        # While we have at least two characters to place
        while len(maxHeap) > 1:
             # Pop two most frequent characters
            cnt1, ch1 = heapq.heappop(maxHeap)
            cnt2, ch2 = heapq.heappop(maxHeap)

            # Append them to result
            res.append(ch1)
            res.append(ch2)

            # Decrease their counts (remember counts are negative)
            cnt1 += 1
            cnt2 += 1

            # If still have remaining occurrences, push back
            if cnt1 < 0: heapq.heappush(maxHeap, (cnt1,ch1))
            if cnt2 < 0: heapq.heappush(maxHeap, (cnt2,ch2))

        # If one character remains, append it
        if maxHeap:
            cnt, ch = heapq.heappop(maxHeap)
            # It is safe to append this because feasibility was already checked
            res.append(ch)
        
        return "".join(res)