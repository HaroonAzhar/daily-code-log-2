# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        res="/"
        for d in arr:
            if d == "." or d == "": 
                continue
            if d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return res+"/".join(stack)
