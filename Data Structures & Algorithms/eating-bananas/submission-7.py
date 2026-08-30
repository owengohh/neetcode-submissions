class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(rate):
            hours = 0
            for p in piles:
                hours += math.ceil(p / rate)
            return hours

        l, r = 1, max(piles)

        while l < r:
            mid = l + (r-l) // 2
            time_taken = hours(mid)
            if time_taken > h:
                l = mid + 1
            else:
                r = mid
        
        return r
