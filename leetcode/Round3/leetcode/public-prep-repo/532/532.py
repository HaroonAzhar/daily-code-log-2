# 532. K-diff Pairs in an Array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        if k == 0:
            for key,v in c.items():
                if v > 1 : count += 1
        else:
            for key,v in c.items():
                if key+k in c: count += 1
        return count