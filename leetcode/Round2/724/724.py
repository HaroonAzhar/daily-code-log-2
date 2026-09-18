# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pivot = 0
        leftSum, rightSum = 0,total
        while(pivot < len(nums)):
            rightSum -= nums[pivot]
            if(leftSum == rightSum):
                return pivot
            leftSum+=nums[pivot]
            pivot+=1
        return -1