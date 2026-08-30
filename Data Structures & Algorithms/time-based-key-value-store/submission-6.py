from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps are assumed to be non-decreasing for each key;
        # append is O(1)
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.time_map.get(key)
        if not vals:
            return ""
        # extract timestamps for bisect; use bisect_right to get
        # insertion index after any equal timestamps
        times = [t for t, _ in vals]
        i = bisect_right(times, timestamp)
        if i == 0:
            return ""
        return vals[i - 1][1]

