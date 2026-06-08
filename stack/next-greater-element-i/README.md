# Next Greater Element I

## Difficulty

Easy

## Problem Description

Given two arrays nums1 and nums2 where nums1 is a subset of nums2, for each element in nums1 find the first greater element to its right in nums2. If none exists, return -1 for that element.

## Constraints

- 1 <= nums1.length <= nums2.length <= 10^3
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique

## Example Input/Output

Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]

## Step-by-Step Explanation

1. Scan nums2 and compute the next greater element for every value.
2. Use a decreasing stack of values; when a larger value appears, it is the next greater for stack items.
3. Store results in a map for O(1) lookup for nums1.

## Optimized Approach

Build a value-to-next-greater map in one pass over nums2 using a monotonic stack, then map answers for nums1.

## Time Complexity

O(n + m)

## Space Complexity

O(n)
