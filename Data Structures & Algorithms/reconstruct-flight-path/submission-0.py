class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src,dst in sorted(tickets, key=lambda x:x[1], reverse=True): graph[src].append(dst)
        res = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            res.append(airport)

        dfs("JFK")
        return res[::-1]