from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        best = 0
        for value in values:
            if value - 1 not in values:
                current = value
                length = 1
                while current + 1 in values:
                    current += 1
                    length += 1
                best = max(best, length)
        return best

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive([]))
