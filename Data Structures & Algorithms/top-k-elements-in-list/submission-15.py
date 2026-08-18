class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []

        for key, count in counter.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (count, key))
            else:
                heapq.heappush(heap, (count, key))
        
        return list(val[1] for val in heap)