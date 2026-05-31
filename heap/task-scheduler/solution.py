from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for v in counts.values() if v == max_freq)
        frame = (max_freq - 1) * (n + 1) + max_count
        return max(frame, len(tasks))


if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    print(sol.leastInterval(["A"], 3))
