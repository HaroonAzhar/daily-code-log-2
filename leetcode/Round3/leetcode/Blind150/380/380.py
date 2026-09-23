# 380. Insert Delete GetRandom O(1)
import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.data)
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        removeIndex = self.index[val]
        lastValue = self.data[-1]

        self.data[removeIndex] = lastValue
        self.index[lastValue] = removeIndex

        self.data.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)