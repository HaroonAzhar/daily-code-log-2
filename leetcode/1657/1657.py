# 1657. Determine if Two Strings Are Close
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(0,len(arr)):
            count[arr[i]] = count.get(arr[i],0) + 1
        vals = set()
        print(f"counts = {count}")
        for index,(key,val) in enumerate(count.items()):
            if(val in vals): return False
            vals.add(val)
        return True