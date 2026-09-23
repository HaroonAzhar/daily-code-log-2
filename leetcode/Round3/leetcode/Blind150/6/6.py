# 6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1): return s
        rows = {}
        row = 1
        op = 1

        for i in range(len(s)):
            rows[row] = rows.get(row,"") + s[i]
            row += op
            if(row >= numRows):
                op = -1
            elif row <= 1:
                op = 1
        res = "".join(rows.values())
        return res