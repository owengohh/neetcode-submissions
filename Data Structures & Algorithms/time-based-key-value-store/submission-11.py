from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]
        if not vals: return ""
        times = [t for t, _ in vals]

        i = bisect_right(times, timestamp)

        if i == 0:
            return ""
        return vals[i-1][1]