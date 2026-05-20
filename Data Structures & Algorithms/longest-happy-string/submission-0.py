class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []  # Max-heap storing [-count, char]
        
        # Push each character with positive count
        if a > 0: heapq.heappush(maxHeap, (-a,"a"))
        if b > 0: heapq.heappush(maxHeap, (-b,"b"))
        if c > 0: heapq.heappush(maxHeap, (-c,"c"))

        res = []

        while maxHeap:
            # Get character with the highest remaining count
            count1, ch1 = heapq.heappop(maxHeap)

             # If adding this character would make three in a row, use second best
            if len(res) >= 2 and res[-1] == ch1 and res[-2] == ch1:
                 # If no other character is available, we are done
                if not maxHeap: break

                # Take the second most frequent character
                count2, ch2 = heapq.heappop(maxHeap)
                res.append(ch2)
                count2 += 1 # counts are negative, so +1 means one less remaining

                # If still have more of ch2, push it back
                if count2 < 0: heapq.heappush(maxHeap, (count2,ch2))
                # Put ch1 back for future consideration
                heapq.heappush(maxHeap, (count1, ch1))
            
            else:
                # Safe to use the most frequent character
                res.append(ch1)
                count1 += 1 # decrement remaining count

                # If still have more of ch1, push it back
                if count1 < 0: heapq.heappush(maxHeap,(count1, ch1)) 
        return "".join(res)