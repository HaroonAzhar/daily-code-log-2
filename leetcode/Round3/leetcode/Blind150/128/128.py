# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 1
        if n < 2: return len(nums)
        s_nums = sorted(list(set(nums)))
        n = len(s_nums)
        left, right = 0,1
        while(right < n):
            while(right < n and s_nums[right] - s_nums[right - 1] == 1):
                right+=1
            longest = max(longest,right - left)
            left = right
            right += 1
        return longest