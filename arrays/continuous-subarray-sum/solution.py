from typing import List, Dict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False

        remainder_index: Dict[int, int] = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            rem = total % k
            if rem in remainder_index:
                if i - remainder_index[rem] >= 2:
                    return True
            else:
                remainder_index[rem] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))
    print(sol.checkSubarraySum([0, 0], 0))
