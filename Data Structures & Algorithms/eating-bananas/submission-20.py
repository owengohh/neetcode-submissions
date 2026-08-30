class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(rate):
            time = 0
            for p in piles:
                time += math.ceil(p / rate)
            return time

        l, r = 1, max(piles)

        while l < r:
            mid = l + (r-l) // 2
            if time(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l