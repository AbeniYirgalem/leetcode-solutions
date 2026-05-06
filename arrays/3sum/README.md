# 3Sum

**Difficulty:** Medium

## Problem Description

Given an integer array, return all unique triplets [a, b, c] such that a + b + c = 0. The solution set must not contain duplicate triplets.

## Examples

**Input:** nums = [-1,0,1,2,-1,-4]
**Output:** [[-1,-1,2],[-1,0,1]]

**Input:** nums = [0,1,1]
**Output:** []

## Step-by-Step Approach

1. Sort the array.
2. For each index i, use two pointers (left, right) to find pairs that sum to -nums[i].
3. Skip duplicates for i, left, and right to avoid repeated triplets.

## Time and Space Complexity

- **Time:** O(n^2)
- **Space:** O(1) extra space (excluding output)
