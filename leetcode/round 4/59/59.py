# 59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0 for i in range(n)] for i in range(n)]
        l,r = 0, n - 1
        t,b = 0, n - 1
        v = 1
        while(l <= r and t <= b):
            for i in range(l,r+1):
                res[t][i] = v
                v+=1
            t+=1

            for i in range(t,b+1):
                res[i][r] = v
                v+=1
            r-=1
            for i in range(r,l-1,-1):
                res[b][i] = v
                v+=1
            b-=1
            for i in range(b,t-1,-1):
                res[i][l] = v
                v+=1
            l+=1
        return res