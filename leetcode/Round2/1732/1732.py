# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        high=0
        for change in gain:
            alt += change
            high = max(alt,high)
        return high