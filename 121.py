# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        worst = 10000
        
        for price in prices:
            worst = min(price,worst)
            profit = max(profit,price - worst)
        
        return profit