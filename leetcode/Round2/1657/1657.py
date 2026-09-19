# 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2) \
        or len(word1) != len(word2) \
        or sorted(Counter(word1).values()) != sorted(Counter(word2).values()):
            return False


        return True