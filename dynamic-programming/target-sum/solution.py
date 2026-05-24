from typing import List, Dict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp: Dict[int, int] = {0: 1}
        for num in nums:
            next_dp: Dict[int, int] = {}
            for s, count in dp.items():
                next_dp[s + num] = next_dp.get(s + num, 0) + count
                next_dp[s - num] = next_dp.get(s - num, 0) + count
            dp = next_dp
        return dp.get(target, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(sol.findTargetSumWays([1], 1))
    print(sol.findTargetSumWays([0, 0, 0], 0))
