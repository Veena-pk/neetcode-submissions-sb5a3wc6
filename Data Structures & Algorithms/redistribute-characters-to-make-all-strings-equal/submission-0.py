from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total = Counter()

        for word in words:
            total.update(word)

        n = len(words)

        for count in total.values():
            if count % n != 0:
                return False
        return True