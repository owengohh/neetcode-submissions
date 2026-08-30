class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        max_p = 0

        for p in prices:
            if p > min_p:
                max_p = max(max_p, p - min_p)
            else:
                min_p = p
        
        return max_p