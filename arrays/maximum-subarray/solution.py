from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for value in nums[1:]:
            current = max(value, current + value)
            best = max(best, current)
        return best

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArray([1]))
