from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0
        for current in range(1, amount + 1):
            for coin in coins:
                if coin <= current:
                    dp[current] = min(dp[current], dp[current - coin] + 1)
        return -1 if dp[amount] == max_value else dp[amount]

if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))
    print(sol.coinChange([2], 3))
