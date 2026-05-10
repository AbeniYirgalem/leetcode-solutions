import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for value, freq in counts.items():
            heapq.heappush(heap, (freq, value))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for _, value in heap]

if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)))
    print(sol.topKFrequent([1], 1))
