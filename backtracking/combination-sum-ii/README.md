# Combination Sum II

## Difficulty

Medium

## Problem Description

Given a collection of candidate numbers (may contain duplicates) and a target number, return all unique combinations where the candidates sum to target. Each number can be used at most once.

## Constraints

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

## Example Input/Output

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

## Step-by-Step Explanation

1. Sort the candidates so duplicates are adjacent.
2. Backtrack by choosing or skipping each number.
3. Skip duplicates at the same depth to avoid repeated combinations.

## Optimized Approach

Sort and backtrack while skipping duplicate values at the same recursion depth.

## Time Complexity

O(2^n) in the worst case

## Space Complexity

O(n) recursion depth, excluding output
