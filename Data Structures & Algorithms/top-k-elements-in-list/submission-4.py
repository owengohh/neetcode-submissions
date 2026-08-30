class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        heapq.heapify(heap)

        for i, count in counter.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (count, i))
            else:
                heapq.heappush(heap, (count, i))
        
        return [x[1] for x in heap]