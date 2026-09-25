# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        occ = {}
        for i in range(len(nums)):
            if nums[i] in occ:
                prv = occ[nums[i]]
                if abs(prv-i) <= k: 
                    return True
            occ[nums[i]] = i
        return False