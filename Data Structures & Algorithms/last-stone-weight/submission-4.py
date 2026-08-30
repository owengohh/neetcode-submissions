class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            if s1 != s2:
                new_val = abs(s1-s2)
                heapq.heappush(heap, -new_val)
        return -heap[0] if len(heap) > 0 else 0