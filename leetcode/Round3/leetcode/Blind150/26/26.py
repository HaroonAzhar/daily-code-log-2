# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        w, r = 1 , 1
        n = len(nums)
        while ( r < n):
            if (nums[r] != nums[w-1]):
                nums[w] = nums[r]
                w+=1
            r +=1
        return w