class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_reversed = [-stone for stone in stones]
        heapq.heapify(stones_reversed)
        while len(stones_reversed) > 1:
            s1 = -heapq.heappop(stones_reversed)
            s2 = -heapq.heappop(stones_reversed)
            if abs(s1-s2) != 0:
                heapq.heappush(stones_reversed,-abs(s1-s2))
        return -stones_reversed[0] if len(stones_reversed) > 0 else 0
        