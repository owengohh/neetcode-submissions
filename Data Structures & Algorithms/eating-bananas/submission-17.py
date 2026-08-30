class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(rate):
            count = 0
            for p in piles:
                count += math.ceil(p / rate)
            return count
        
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if hours(mid) <= h:
               r = mid
            else:
                l = mid + 1
        return r


