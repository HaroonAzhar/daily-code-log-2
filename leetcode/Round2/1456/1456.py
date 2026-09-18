# 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowels, i, n = 0, 0, len(s)
        l,r = 0,0
        vowels = set("aeiou")
        while(r < k):
            if s[r] in vowels:
                maxVowels+=1
            r+=1
            wVowels = maxVowels
        while(r < n):
            if s[r] in vowels:
                wVowels +=1
            if s[l] in vowels:
                wVowels -=1
            maxVowels= max(maxVowels,wVowels)
            l+=1
            r+=1
        return maxVowels