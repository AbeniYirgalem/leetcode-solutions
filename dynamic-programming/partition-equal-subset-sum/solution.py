from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition([1, 5, 11, 5]))
    print(sol.canPartition([1, 2, 3, 5]))
    print(sol.canPartition([2, 2, 1, 1]))
