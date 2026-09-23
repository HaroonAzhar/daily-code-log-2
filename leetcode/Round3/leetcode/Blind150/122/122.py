class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        cVal = prices[0]
        n = len(prices)
        for i in prices[1:]:
            if i - cVal  > 0:
                totalProfit += i - cVal
            cVal = i
            if cVal > i:
                cVal = i
        return totalProfit