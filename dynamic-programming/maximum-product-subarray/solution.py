from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_here = nums[0]
        min_here = nums[0]
        best = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_here, min_here = min_here, max_here
            max_here = max(num, max_here * num)
            min_here = min(num, min_here * num)
            best = max(best, max_here)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))
    print(sol.maxProduct([-2, 0, -1]))
    print(sol.maxProduct([0, 2]))
