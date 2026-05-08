# Permutations

**Difficulty:** Medium

## Problem Description

Given a collection of distinct integers, return all possible permutations.

## Examples

**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

**Input:** nums = [0,1]
**Output:** [[0,1],[1,0]]

## Step-by-Step Approach

1. Use backtracking with a used set.
2. Build permutations by choosing an unused number at each step.
3. When the path length equals nums length, record it.

## Time and Space Complexity

- **Time:** O(n \* n!)
- **Space:** O(n)
