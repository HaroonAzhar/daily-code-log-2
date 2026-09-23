# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        for p in prices[1:]:
            if buyPrice > p:
                buyPrice = p
            maxProfit = max(maxProfit, p - buyPrice)
        return maxProfit