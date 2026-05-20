class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qR = deque()
        qD = deque()

        for i,ch in enumerate(senate):
            if ch == 'R': qR.append(i)
            else: qD.append(i)

        while qR and qD:
            r = qR.popleft()
            d = qD.popleft()

            if r < d: qR.append(r+len(senate))
            else: qD.append(d+len(senate))

        return "Radiant" if qR else "Dire"