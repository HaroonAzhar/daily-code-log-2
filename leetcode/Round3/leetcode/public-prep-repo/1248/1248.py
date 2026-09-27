# 1248. Count Number of Nice Subarrays
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        l, r = 0,0
        n = len(nums)
        nice = 0
        wcount = 0
        variants = 0
        while(r < n):
            if nums[r] % 2 == 1:
                wcount+=1
                variants = 0
            while wcount == k:
                variants +=1
                if nums[l] % 2 == 1: wcount -=1
                l+=1
            nice+=variants
            r+=1
        return nice