# Partition Equal Subset Sum

## Difficulty

Medium

## Problem Description

Given an array of positive integers, determine if it can be partitioned into two subsets with equal sum.

## Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

## Example Input/Output

Input: nums = [1,5,11,5]
Output: true

## Step-by-Step Explanation

1. Compute total sum; if odd, return false.
2. Use a boolean dp to track achievable sums up to target.
3. If target is achievable, the array can be partitioned.

## Optimized Approach

1D subset-sum DP with reverse iteration.

## Time Complexity

O(n \* target)

## Space Complexity

O(target)
