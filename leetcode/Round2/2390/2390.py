# 2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i,k in enumerate(s):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)