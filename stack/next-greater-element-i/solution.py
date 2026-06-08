from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack: List[int] = []

        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        return [next_greater.get(num, -1) for num in nums1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(sol.nextGreaterElement([2, 4], [1, 2, 3, 4]))
    print(sol.nextGreaterElement([1], [1]))
