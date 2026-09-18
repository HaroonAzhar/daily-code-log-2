# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxV =0
        l,r = 0, len(height) - 1
        while(l<r):
            current = (r - l) * min(height[l], height[r])
            maxV = max(maxV,current)
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
        return maxV 