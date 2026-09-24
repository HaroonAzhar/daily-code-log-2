# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch2id = {}
        n = len(s)
        left, right = 0,0
        longest = 0
        while( right < n):
            if s[right] not in ch2id or ch2id[s[right]] < left:
                ch2id[s[right]] = right
                longest = max(longest, right - left +1)
                right+=1
            else:
                left = ch2id[s[right]] + 1
                ch2id[s[right]] = right
                right+=1
        return longest
