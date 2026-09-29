# 2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = Counter()
        rows = cols = len(grid)
        total = 0
        for row in grid:
            c[tuple(row)] += 1
            
        for i in range(rows):
            cc = []
            for j in range(cols):
                cc.append(grid[j][i])
            total += c[tuple(cc)]
        return total