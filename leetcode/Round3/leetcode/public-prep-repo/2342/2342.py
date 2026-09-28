# 2342. Max Sum of a Pair With Equal Sum of Digits
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        m = defaultdict(lambda: -1)
        pairMax = -1
        for num in nums:
            s = sum(int(d) for d in str(num))
            if m[s] > 0:
                s2 = num + m[s]
                pairMax = max(pairMax,s2)
                m[s] = max(num,m[s])
            else:
                m[s] = num
        return pairMax
        