# Subsets

**Difficulty:** Medium

## Problem Description

Given an integer array of unique elements, return all possible subsets.

## Examples

**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

**Input:** nums = [0]
**Output:** [[],[0]]

## Step-by-Step Approach

1. Use backtracking to decide include/exclude for each element.
2. Record the current path at every step.

## Time and Space Complexity

- **Time:** O(n \* 2^n)
- **Space:** O(n)
