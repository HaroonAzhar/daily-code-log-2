# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals = sorted(intervals,key=lambda x:x[0])
        curEnd = intervals[0][1]
        curstart = intervals[0][0]
        res = []
        for start,end in intervals:
            if curEnd >= start:
                curEnd = max(curEnd,end)
            else:
                res.append([curstart,curEnd])
                curstart,curEnd = start, end
        res.append([curstart,curEnd])
        return res