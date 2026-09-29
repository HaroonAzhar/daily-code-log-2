# 1807. Evaluate the Bracket Pairs of a String
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        d = dict(knowledge)
        res =""
        i  = 0
        n = len(s)
        while i < n:
            s[i]
            if s[i] == "(":
                key = ""
                while s[i] != ")":
                    key+=s[i]
                    i+=1
                if key[1:] in d:
                    res+= d[key[1:]]
                else:
                    res+="?"
                i+=1
            else:
                res+=s[i]
                i+=1
        return res