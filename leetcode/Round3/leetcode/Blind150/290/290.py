# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if(len(words) != len(pattern)): return False
        ch2w = {}
        for i in range(len(pattern)):
            if pattern[i] in ch2w:
                if ch2w[pattern[i]] != words[i]:
                    return False
            elif words[i] in ch2w.values():
                return False
                
            ch2w[pattern[i]] = words[i]
        return True