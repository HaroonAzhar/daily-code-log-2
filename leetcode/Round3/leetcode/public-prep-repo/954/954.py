# 954. Array of Doubled Pairs
class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        n = [v for v in arr if v < 0]
        p = [v for v in arr if v >= 0]
        narr = sorted(n,reverse=True) + sorted(p)
        c = Counter(narr)
        for i in narr:
            if c[i] == 0: continue
            if c[2*i] == 0: return False
            c[i] -= 1
            c[2*i] -= 1
        return True