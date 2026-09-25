# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        res = []
        n = len(nums)
        left, right = 0,0
        while(right < n -1):
            if right < n and nums[right] + 1 == nums[right+1]:
                right+=1
            else:
                if nums[left] == nums[right]:
                    res.append(f"{nums[right]}")
                else:
                    res.append(f"{nums[left]}->{nums[right]}")
                left = right + 1
                right += 1
        if nums[left] == nums[right]:
            res.append(f"{nums[right]}")
        else:
            res.append(f"{nums[left]}->{nums[right]}")
        return res