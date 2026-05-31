from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, _ in items[:k]]


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    print(sol.topKFrequent(["a", "b", "c"], 2))
