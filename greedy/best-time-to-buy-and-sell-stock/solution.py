from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                best = max(best, price - min_price)
        return best

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit([7, 6, 4, 3, 1]))
