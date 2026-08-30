class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i, price in enumerate(prices):
            if price < min_price:
                min_price = min(price, min_price)
            else:
                res = max(price - min_price, res) 
        return res