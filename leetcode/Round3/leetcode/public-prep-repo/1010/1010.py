# 1010. Pairs of Songs With Total Durations Divisible by 60
class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        needing = {}
        count=0
        for t in time:
            rm = t % 60
            need = (60 - rm) % 60

            count += needing.get(need, 0)

            needing[rm] = needing.get(rm, 0) + 1

        return count