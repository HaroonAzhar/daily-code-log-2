# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[1]*len(nums)
        prefix=1
        suffix=1
        for i in range(len(nums)):
            op[i]=prefix
            prefix*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            op[i]*=suffix
            suffix*=nums[i]
            
        return op