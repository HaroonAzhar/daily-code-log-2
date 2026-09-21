# 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.added = []
        self.smallest = 1
        self.arePresent = set()
            

    def popSmallest(self) -> int:
        if self.added:
            val = heapq.heappop(self.added)
            self.arePresent.remove(val)
            return val
        else:
            self.smallest += 1
            return self.smallest - 1

            

    def addBack(self, num: int) -> None:
        if self.smallest <= num or num in self.arePresent:
            return
        else:
            heapq.heappush(self.added,num)
            self.arePresent.add(num)

