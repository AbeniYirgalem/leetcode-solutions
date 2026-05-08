from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        used = [False] * len(nums)

        def backtrack(path: List[int]) -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i, value in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(value)
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    print(sol.permute([0]))
