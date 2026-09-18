# 1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        maxOnes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maxOnes = max(maxOnes, right - left)

        return maxOnes