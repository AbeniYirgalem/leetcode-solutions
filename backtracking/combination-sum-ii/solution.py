from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            prev = None
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                if candidates[i] > remaining:
                    break
                prev = candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
    print(sol.combinationSum2([1, 1, 1], 2))
