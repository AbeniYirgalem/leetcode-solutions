from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols
        dp[0] = grid[0][0]
        for c in range(1, cols):
            dp[c] = dp[c - 1] + grid[0][c]
        for r in range(1, rows):
            dp[0] += grid[r][0]
            for c in range(1, cols):
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))
    print(sol.minPathSum([[5]]))
