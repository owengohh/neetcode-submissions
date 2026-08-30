
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for i, (x, y) in enumerate(points):
            if len(heap) >= k:
                heapq.heappushpop(heap, (-(x**2+y**2), i))
            else:
                heapq.heappush(heap, (-(x**2+y**2), i))
        
        res = []
        for _, idx in heap:
            res.append(points[idx])
        
        return res
            

        
