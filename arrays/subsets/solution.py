from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(start: int, path: List[int]) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([0]))
