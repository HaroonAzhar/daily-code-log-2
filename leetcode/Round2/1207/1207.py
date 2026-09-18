# 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        times = {}
        for num in arr:
            count[num] = count.get(num,0) + 1
        for val in count.values():
            if(times.get(val,False)): return False
            times[val] = 1
        return True