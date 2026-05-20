class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                if ch not in indegree: indegree[ch] = 0

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ""

            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break

        q = deque([ch for ch in indegree if indegree[ch] == 0])
        order = []

        while q:
            ch = q.popleft()
            order.append(ch)

            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0: q.append(nei)

        if len(order) == len(indegree): return "".join(order)
        return ""