from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack: List[int] = []

        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                prev = stack.pop()
                result[prev] = nums[idx]
            if i < n:
                stack.append(idx)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElements([1, 2, 1]))
    print(sol.nextGreaterElements([3, 8, 4, 1, 2]))
    print(sol.nextGreaterElements([5]))
