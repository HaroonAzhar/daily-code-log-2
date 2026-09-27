# 3159. Find Occurrences of an Element in an Array
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occ = []
        res = []
        for k,v in enumerate(nums):
            if v == x: occ.append(k)
        for s in queries:
            if s > len(occ): 
                res.append(-1)
            else:
                res.append(occ[s-1])
        return res