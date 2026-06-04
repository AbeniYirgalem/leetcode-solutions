# Minimum Size Subarray Sum

## Difficulty

Medium

## Problem Description

Given an array of positive integers and a target sum, find the minimal length of a contiguous subarray with sum >= target. Return 0 if none exists.

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= target <= 10^9

## Example Input/Output

Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2

## Step-by-Step Explanation

1. Use a sliding window with two pointers.
2. Expand the right pointer to reach or exceed the target.
3. Shrink the left pointer to minimize the window while keeping sum >= target.

## Optimized Approach

Sliding window in one pass.

## Time Complexity

O(n)

## Space Complexity

O(1)
