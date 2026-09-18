# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2, c = len(word1), len(word2), 0 
        res = ''
        while(c < l1 and c < l2):
            res += word1[c]
            res+= word2[c]
            c+=1
        if(l1 == l2): return res
        if(l1>l2):
            while(c<l1):
                res+=word1[c]
                c+=1
        else:
            while(c<l2):
                res+=word2[c]
                c+=1
        return res
    