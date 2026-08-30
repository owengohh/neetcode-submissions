class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        min_heap = [(0, 0, src)]

        dist = {}

        while min_heap:
            w1, s1, n1 = heapq.heappop(min_heap)
            if n1 == dst:
                return w1
            if s1 > k:
                continue
     
            if (n1, s1) in dist and dist[(n1, s1)] <= w1:
                continue
            dist[(n1, s1)] = w1
            for n2, w2 in adj[n1]:
                heapq.heappush(min_heap, (w2 + w1, s1+1, n2))
        return -1