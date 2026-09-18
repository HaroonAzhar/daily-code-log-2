# 2215. Find the Difference of Two Arrays
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1 = set(nums1)
    s2 = set(nums2)
    ar1 = []
    for item in s1:
        if item in s2:
            s2.remove(item)
        else:
            ar1.append(item)
    return [ar1,list(s2)]