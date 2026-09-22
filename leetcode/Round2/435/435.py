# 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        currEnd = -math.inf
        count = 0
        for start,end in intervals:
            if start >= currEnd:
                currEnd = end
            else:
                count+=1
        return count