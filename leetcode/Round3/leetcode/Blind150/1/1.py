# 1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        differences = {}
        for index,value in enumerate(nums):
            diff = target - value
            diff_index = differences.get(diff, False)
            if(diff_index):
                return [diff_index - 1,index]
            else:
                differences[value] = index + 1