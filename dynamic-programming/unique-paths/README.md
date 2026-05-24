# Unique Paths

## Difficulty

Medium

## Problem Description

A robot is located at the top-left of an m x n grid and can move only right or down. Return the number of unique paths to the bottom-right.

## Constraints

- 1 <= m, n <= 100

## Example Input/Output

Input: m = 3, n = 7
Output: 28

## Step-by-Step Explanation

1. Use dp where dp[j] is paths to current cell in the row.
2. Update dp[j] = dp[j] + dp[j-1] as you move across columns.

## Optimized Approach

1D DP that reuses the previous row.

## Time Complexity

O(m\*n)

## Space Complexity

O(n)
