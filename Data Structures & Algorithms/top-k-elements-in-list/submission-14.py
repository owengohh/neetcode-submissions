class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num in counter.keys():
            heapq.heappush(heap, (counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res