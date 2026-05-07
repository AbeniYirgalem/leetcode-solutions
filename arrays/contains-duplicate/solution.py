from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for value in nums:
            if value in seen:
                return True
            seen.add(value)
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))
    print(sol.containsDuplicate([1, 2, 3, 4]))
