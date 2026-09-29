# 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sint = sorted(intervals,key=lambda x:x[1])
        clash=0
        cstart, cend = sint[0][0], sint[0][1]
        for s,e in sint[1:]:
            if  s >= cend:
                cend = e
            else:
                clash+=1
        return clash