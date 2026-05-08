from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for value in nums:
            if value != 0:
                nums[write] = value
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    sol = Solution()
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)
    nums2 = [0]
    sol.moveZeroes(nums2)
    print(nums2)
