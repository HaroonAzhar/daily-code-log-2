# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        w,r, n = 1,1, len(nums)
        while r < n:
            if nums[r] != nums[w-1]:
                nums[w] = nums[r]
                w+=1
            r+=1
        return w