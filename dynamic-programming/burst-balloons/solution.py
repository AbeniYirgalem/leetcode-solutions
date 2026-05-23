from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        vals = [1] + [n for n in nums if n > 0] + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                best = 0
                for k in range(left + 1, right):
                    coins = vals[left] * vals[k] * vals[right]
                    coins += dp[left][k] + dp[k][right]
                    best = max(best, coins)
                dp[left][right] = best
        return dp[0][n - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCoins([3, 1, 5, 8]))
    print(sol.maxCoins([1, 5]))
    print(sol.maxCoins([0, 0, 0]))
