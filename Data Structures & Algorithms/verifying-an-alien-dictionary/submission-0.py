class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            min_len = min(len(w1), len(w2))
            j = 0
            while j < min_len and w1[j] == w2[j]: j += 1

            if j == min_len:
                if len(w1) > len(w2): return False
            else:
                if rank[w1[j]] > rank[w2[j]]: return False
        return True