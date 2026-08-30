class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(rate):
            count = 0
            for pile in piles:
                count += math.ceil(pile / rate)
            return count
        
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l) // 2
            if hours(mid) > h:
                l = mid + 1
            else:
                r = mid
        return l