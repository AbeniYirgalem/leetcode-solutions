# Maximum Product Subarray

## Difficulty

Medium

## Problem Description

Given an integer array, find the contiguous subarray with the largest product.

## Constraints

- 1 <= nums.length <= 2 \* 10^4
- -10 <= nums[i] <= 10

## Example Input/Output

Input: nums = [2,3,-2,4]
Output: 6

## Step-by-Step Explanation

1. Track max and min products ending at each position.
2. A negative value can swap max and min.
3. Update the global maximum.

## Optimized Approach

Greedy DP with two running values.

## Time Complexity

O(n)

## Space Complexity

O(1)
