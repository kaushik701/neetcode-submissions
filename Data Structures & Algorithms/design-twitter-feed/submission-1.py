import heapq
class Twitter:

    def __init__(self):
        self.count=0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res: List[int] = []
        minHeap: list[list[int | None]] = []

        # A user should see their own tweets
        self.followMap[userId].add(userId)

        # For each followee, push their most recent tweet into the heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                timestamp, tweetId = self.tweetMap[followeeId][index]
                # Heap entry: [timestamp, tweetId, followeeId, next_index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index - 1])

        # Pop up to 10 most recent tweets
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # If this followee has older tweets, push the next one
            if index >= 0:
                timestamp, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: self.followMap[followerId].remove(followeeId)
