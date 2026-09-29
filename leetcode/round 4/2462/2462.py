# 2462. Total Cost to Hire K Workers
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        l, r  = 0, n -1
        hl = []
        hr = []
        mcost = 0
        # fill left heap
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(hl, (costs[l], l))
                l += 1

        # fill right heap
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(hr, (costs[r], r))
                r -= 1

            

        for i in range(k):
            v1 = i1 = v2 = i2 = math.inf

            if hl:
                v1, i1 = hl[0]

            if hr:
                v2, i2 = hr[0]

            if v1 <= v2:
                heapq.heappop(hl)
                mcost += v1

                if l <= r:
                    heapq.heappush(hl, (costs[l], l))
                    l += 1

            else:
                heapq.heappop(hr)
                mcost += v2

                if l <= r:
                    heapq.heappush(hr, (costs[r], r))
                    r -= 1
        return mcost