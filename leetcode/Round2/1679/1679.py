# 1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diffMap = {}
        pairs = 0
        for num in nums:
            diff = k - num
            if(diffMap.get(diff,False)):
                diffMap[diff] = diffMap.get(diff) - 1
                pairs+=1
            else:
                diffMap[num] = diffMap.get(num,0) +1
        return pairs