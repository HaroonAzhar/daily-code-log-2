# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        i = 0
        n = len(cost)
        fuel = 0
        station = 0
        while(i < n):
            fuel+= gas[i] - cost[i]
            if fuel < 0:
                station = i + 1
                fuel = 0
            i+=1
        return station