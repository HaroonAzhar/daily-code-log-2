# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        lproduct , rproduct = 1, 1
        for ind,num in enumerate(nums):
            res[ind] = lproduct
            lproduct *= num
        for ind in range(n-1,-1,-1):
            res[ind] *= rproduct
            rproduct *= nums[ind]
        return res