# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for el in strs:
            key = "".join(sorted(el))
            retrieved = groups.get(key,[])
            retrieved.append(el)
            groups[key] = retrieved
        return list(groups.values())