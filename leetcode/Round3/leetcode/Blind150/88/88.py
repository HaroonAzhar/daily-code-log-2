# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1 = m - 1 
        i2 = n - 1
        r = len(nums1) - 1
        while (i1 >= 0 and i2 >=0):
            if nums1[i1] > nums2[i2]:
                nums1[r] = nums1[i1]
                i1 -= 1
            else:
                nums1[r] = nums2[i2]
                i2 -= 1
            r-=1
        if(i2 < 0):
            while(i1 >= 0):
                nums1[r] = nums1[i1]
                r -= 1
                i1 -= 1
        else:
            while(i2 >= 0):
                nums1[r] = nums2[i2]
                r-=1
                i2-=1