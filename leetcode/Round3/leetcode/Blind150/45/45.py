# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0
        n = len(nums) 
        while(far < n - 1):
            farthest = 0
            for i in range(near,far+1):
                farthest = max(farthest, nums[i]+i)
            near = far + 1
            far = farthest
            jumps += 1
        return jumps