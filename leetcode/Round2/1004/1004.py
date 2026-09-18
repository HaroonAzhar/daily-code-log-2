# 1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, right, n = 0,0, len(nums)
        zeros = 0
        longest = 0
        while(right < n):
            if nums[right] == 0:
                zeros +=1

            while(zeros > k):
                if nums[left] == 0:
                    zeros -= 1
                left+=1
            longest = max(longest, right - left + 1)
            right+=1
        return longest