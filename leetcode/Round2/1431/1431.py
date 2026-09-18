# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxVal = max(candies)
        res = []
        for i in range(len(candies)):
            res.append(candies[i]+extraCandies >= maxVal)
        return res