from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start < prev_end:
                removals += 1
            else:
                prev_end = end
        return removals


if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(sol.eraseOverlapIntervals([[1, 2], [2, 3]]))
