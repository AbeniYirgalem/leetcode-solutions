# Maximum Subarray

**Difficulty:** Medium

## Problem Description

Given an integer array, find the contiguous subarray with the largest sum and return that sum.

## Examples

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6

**Input:** nums = [1]
**Output:** 1

## Step-by-Step Approach

1. Use Kadane's algorithm to track the best sum ending at each position.
2. Either extend the previous subarray or start fresh at the current element.
3. Track the global maximum over all positions.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
