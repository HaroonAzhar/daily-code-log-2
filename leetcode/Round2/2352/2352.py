# 2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = {}
        n = len(grid)
        pairs = 0

        for row in grid:
            key = tuple(row)
            dic[key] = dic.get(key, 0) + 1

        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))

            if col in dic:
                pairs += dic[col]

        return pairs