from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half - i
            left_max_a = nums1[i - 1] if i > 0 else float("-inf")
            right_min_a = nums1[i] if i < m else float("inf")
            left_max_b = nums2[j - 1] if j > 0 else float("-inf")
            right_min_b = nums2[j] if j < n else float("inf")
            if left_max_a <= right_min_b and left_max_b <= right_min_a:
                if (m + n) % 2 == 0:
                    return (max(left_max_a, left_max_b) + min(right_min_a, right_min_b)) / 2
                return float(max(left_max_a, left_max_b))
            if left_max_a > right_min_b:
                right = i - 1
            else:
                left = i + 1
        return 0.0

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
