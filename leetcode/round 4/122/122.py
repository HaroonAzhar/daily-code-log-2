# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tp = 0
        cp = prices[0]

        for p in prices[1:]:
            if p > cp:
                tp += p - cp
            cp = p

        return tp