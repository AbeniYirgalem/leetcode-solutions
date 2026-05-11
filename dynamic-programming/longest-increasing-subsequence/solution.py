from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []
        for value in nums:
            i = bisect_left(tails, value)
            if i == len(tails):
                tails.append(value)
            else:
                tails[i] = value
        return len(tails)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
