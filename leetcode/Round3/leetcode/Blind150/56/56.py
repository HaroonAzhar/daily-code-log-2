# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        n = len(intervals)
        if n == 1: return intervals
        res = []
        intervals.sort(key= lambda x: x[0] )
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if currEnd >= start:
                currEnd = max(currEnd,end)
            else:
                res.append([currStart,currEnd])
                currStart = start
                currEnd = end
        res.append([currStart,currEnd])
        return res
        