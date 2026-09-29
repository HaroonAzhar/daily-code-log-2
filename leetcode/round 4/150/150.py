# 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                q = stack.pop() + stack.pop()
                stack.append(q)
            elif ch == "-":
                f , s = stack.pop(),stack.pop()
                stack.append(s - f)
            elif ch == "/":
                f , s = stack.pop(),stack.pop()
                stack.append(int(s / f))
            elif ch == "*":
                q = stack.pop() * stack.pop()
                stack.append(q)
            else:
                stack.append(int(ch))
        return stack[0]
        