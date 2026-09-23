# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        explorer = 0
        n = len(nums)
        while( explorer < n):
            if nums[explorer] == val:
                nums[explorer] = nums[n - 1]
                n -= 1
            else:
                explorer += 1
        return n