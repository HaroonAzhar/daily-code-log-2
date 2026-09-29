# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r, safe = n - 2, n-1
        while(r>=0):
            if r+nums[r] >= safe:
                safe = r
            r-=1
        return True if safe == 0 else False