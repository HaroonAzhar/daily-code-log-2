# 2300. Successful Pairs of Spells and Potions
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        res = []
        potions = sorted(potions)
        for spell in spells:
            res.append(self.search(spell,potions,success))
        return res

    def search(self, ss, p,t):
        n = len(p)
        l, r = 0, n - 1
        id = -1
        while(l <= r):
            mid = (l+r) // 2
            sp = ss * p[mid]
            if sp >= t:
                id = mid
                r = mid - 1
            else:
                l = mid + 1
        return n - id if id != -1 else 0