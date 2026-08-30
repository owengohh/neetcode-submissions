class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        heapq.heapify(heap)

        for key in counter:
            if len(heap) >= k:
                heapq.heappushpop(heap, [counter[key], key])
            else:
                heapq.heappush(heap, [counter[key], key])
        return [x[1] for x in heap]