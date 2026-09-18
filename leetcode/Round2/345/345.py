# 345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        all_vowels = set("aeiouAEIOU")
        for ch in s:
            if ch in all_vowels: stack.append(ch)
        res=""
        for ch in s:
            if ch in all_vowels:
                res+=stack.pop()
            else:
                res+=ch
        return res