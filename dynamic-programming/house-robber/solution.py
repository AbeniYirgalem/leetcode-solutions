from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for value in nums:
            prev, curr = curr, max(curr, prev + value)
        return curr

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2]))
