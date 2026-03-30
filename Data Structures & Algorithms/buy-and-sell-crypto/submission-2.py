class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        profit = 0
        for price in prices:
            min_buy = min(min_buy,price)
            current_profit = price - min_buy
            profit = max(profit, current_profit)
        return profit