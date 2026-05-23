# Minimum Path Sum

## Difficulty

Medium

## Problem Description

Given a grid of non-negative numbers, find a path from top-left to bottom-right which minimizes the sum of all numbers along its path.

## Constraints

- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100

## Example Input/Output

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7

## Step-by-Step Explanation

1. Use DP where dp[j] is the min sum to reach current cell.
2. Update dp[j] using min of top and left paths.

## Optimized Approach

1D DP rolling array.

## Time Complexity

O(m\*n)

## Space Complexity

O(n)
