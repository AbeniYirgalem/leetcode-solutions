from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        best = float("inf")

        for right, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                best = min(best, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if best == float("inf") else int(best)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen(4, [1, 4, 4]))
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1]))
