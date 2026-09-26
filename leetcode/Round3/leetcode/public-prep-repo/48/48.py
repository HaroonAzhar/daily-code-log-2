# 48. Rotate Image
class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(i+1,col):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for i in range(row):
            for j in range(col // 2):
                mat[i][j],mat[i][row-j-1] = mat[i][row-j-1],mat[i][j]