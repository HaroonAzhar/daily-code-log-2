# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        wSum = 0
        maxAvg = -math.inf
        l,r = 0,0
        while(r < k):
            wSum+=nums[r]
            maxAvg = round(wSum/k,5)
            r+=1
        while(r < len(nums)):
            wSum+=nums[r]
            wSum-=nums[l]
            l+=1
            r+=1
            maxAvg = max(maxAvg,round(wSum/k,5))
        return maxAvg