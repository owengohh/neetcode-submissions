class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        

        heap = []
        heapq.heapify(heap)

        for key, value in counter.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (value, key))
            else:
                heapq.heappush(heap, (value, key))
        
        return [i[1] for i in heap]

