from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def hours_needed(speed: int) -> int:
            total = 0
            for pile in piles:
                total += (pile + speed - 1) // speed
            return total

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3, 6, 7, 11], 8))
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))
