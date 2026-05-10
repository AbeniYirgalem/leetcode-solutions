from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_value = {}
        for i, value in enumerate(nums):
            need = target - value
            if need in index_by_value:
                return [index_by_value[need], i]
            index_by_value[value] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([3, 2, 4], 6))
