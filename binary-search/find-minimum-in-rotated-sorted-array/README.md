# Find Minimum in Rotated Sorted Array

## Difficulty

Medium

## Problem Description

Given a rotated sorted array with unique elements, return the minimum element.

## Constraints

- 1 <= nums.length <= 5000
- -5000 <= nums[i] <= 5000
- All elements are unique

## Example Input/Output

Input: nums = [3, 4, 5, 1, 2]
Output: 1

## Step-by-Step Explanation

1. Use binary search to locate the pivot.
2. If mid is greater than the right, the minimum is on the right.
3. Otherwise, the minimum is on the left including mid.

## Optimized Approach

Binary search on the rotation point.

## Time Complexity

O(log n)

## Space Complexity

O(1)
