# Combination Sum

**Difficulty:** Medium

## Problem Description

Given an array of distinct integers and a target, return all unique combinations where the numbers sum to target. Each number may be used unlimited times.

## Examples

**Input:** candidates = [2,3,6,7], target = 7
**Output:** [[2,2,3],[7]]

**Input:** candidates = [2,3,5], target = 8
**Output:** [[2,2,2,2],[2,3,3],[3,5]]

## Step-by-Step Approach

1. Use backtracking to build combinations.
2. Keep a running total and start index to avoid duplicates.
3. If the total reaches the target, record the combination.

## Time and Space Complexity

- **Time:** Exponential in number of combinations
- **Space:** O(target) recursion depth
