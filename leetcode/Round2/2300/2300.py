# 2300. Successful Pairs of Spells and Potions
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        sortedP = potions.sort()
        n= len(potions) - 1
        res = []
        for spell in spells:
            idx =  self.bs(spell,success, potions)
            res.append(len(potions) - idx if idx != -1 else 0)
        return res
    def bs(self, strength, target, potions):
        start,end = 0, len(potions) -1
        idx = -1
        while(start <= end):
            mid = (start +end)//2
            prod = strength * potions[mid]
            if prod >= target:
                idx = mid
                end = mid -1
            else:
                start = mid +1
        return idx