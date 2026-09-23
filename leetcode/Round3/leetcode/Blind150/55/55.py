# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        safeInd = n - 1
        for i in range(n-1,-1,-1):
            if (i + nums[i]) >= safeInd:
                safeInd = i
        return True if safeInd == 0 else False