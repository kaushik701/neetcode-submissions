class CountSquares:

    def __init__(self):
        self.pointCount = Counter()

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1,y1 = point
        ans = 0

        for (x2,y2), cnt in self.pointCount.items():
            if x1 == x2 or y1 == y2: continue
            if abs(x1-x2) != abs(y1-y2): continue
            ans += cnt * self.pointCount[(x1,y2)] * self.pointCount[(x2,y1)]
        return ans 
