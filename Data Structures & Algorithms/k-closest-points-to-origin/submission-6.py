
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x1, y1 in points:
            dist = (x1 ** 2 + y1 ** 2)
            heapq.heappush(heap, (dist, (x1, y1)))

        res = []

        for i in range(k):
            val = heapq.heappop(heap)
            res.append(list(val[1]))
        
        return res
        