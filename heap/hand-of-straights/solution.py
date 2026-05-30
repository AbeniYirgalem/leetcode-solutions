from typing import List
from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            for val in range(start, start + groupSize):
                if count[val] == 0:
                    return False
                count[val] -= 1
                if count[val] == 0:
                    if val != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print(sol.isNStraightHand([1, 2, 3, 4, 5], 4))
    print(sol.isNStraightHand([1, 2, 3, 4], 1))
