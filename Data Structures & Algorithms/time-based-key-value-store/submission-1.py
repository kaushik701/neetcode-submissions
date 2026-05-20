class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""

        arr = self.store[key] #stores the ts,val as the value for the given key
        l,r = 0,len(arr)-1
        res = ""

        while l <= r:
            mid = (l+r) // 2
            ts,val = arr[mid]

            if ts <= timestamp:
                res = val
                l = mid+1
            else: r = mid-1
        return res

