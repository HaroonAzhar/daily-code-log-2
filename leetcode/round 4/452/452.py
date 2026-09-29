# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        spoints = sorted(points, key=lambda x:x[0])
        cstart, cend = spoints[0][0], spoints[0][1]
        shots = 1
        for i in spoints[1:]:
            if cend >= i[0]:
                cend = min(i[1],cend)
            else:
                shots+=1
                cstart = i[0]
                cend = i[1]
        return shots