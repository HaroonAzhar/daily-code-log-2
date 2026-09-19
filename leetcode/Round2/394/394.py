# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        currChar =''
        currNumb = 0
        result = ''
        stack = []
        for ch in s:
            if ch.isdigit():
                currNumb= (currNumb*10) + int(ch)
            elif ch == "[":
                stack.append((currChar, currNumb))
                currChar=''
                currNumb=0
            elif ch == "]":
                previousText, num = stack.pop()
                currChar = previousText + (currChar*num)
            else:
                currChar+=ch
        return currChar