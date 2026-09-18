# 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0,1,1,2]
        N = n
        while n>=4:
            curr = [x+1 for x in dp]
            dp += curr
            n = n//2
        return dp[:N+1]



        