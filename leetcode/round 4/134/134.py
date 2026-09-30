# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        i = s = f = 0
        n = len(gas)

        while( i < n):
            f += gas[i] - cost[i]
            if f < 0:
                s = i+1
                f = 0
            i+=1
        return s