# 3160. Find the Number of Distinct Colors Among the Balls
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        coloredballs = defaultdict(int)
        cc = defaultdict(int)
        res = []

        for ball, color in queries:

            if ball in coloredballs:
                bc = coloredballs[ball]

                if bc != color:
                    cc[bc] -= 1

                    if cc[bc] == 0:
                        del cc[bc]

                    coloredballs[ball] = color
                    cc[color] += 1

            else:
                coloredballs[ball] = color
                cc[color] += 1

            res.append(len(cc))

        return res