# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(s) > len(t): return False
        si,ti = 0 , 0
        while(si<len(s) and ti < len(t)):
            if t[ti] == s[si]:
                ti+=1
                si+=1
            else:
                ti+=1
        return True if si>=len(s) else False