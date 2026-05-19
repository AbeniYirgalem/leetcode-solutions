from typing import List, Dict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        freq: Dict[int, int] = {0: 1}

        for num in nums:
            prefix += num
            count += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))
    print(sol.subarraySum([1, 2, 3], 3))
    print(sol.subarraySum([1, -1, 0], 0))
