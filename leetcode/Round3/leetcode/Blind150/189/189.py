# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k != 0:
            nums[:k],nums[k:] = nums[n-k:],nums[:n-k]