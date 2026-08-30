class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for count, num in heap:
            res.append(num)
        
        return res