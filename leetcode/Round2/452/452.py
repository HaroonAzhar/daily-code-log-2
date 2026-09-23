# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
    points.sort(key = lambda x: x[0])
    shots = 1
    currEnd = points[0][1]
    for start,end in points[1:]:
        if start>currEnd:
            shots+=1
            currEnd = end
        else:
            currEnd = min(end,currEnd)
    return shots