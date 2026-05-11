# Longest Increasing Subsequence

**Difficulty:** Medium

## Problem Description

Given an integer array, return the length of the longest strictly increasing subsequence.

## Examples

**Input:** nums = [10,9,2,5,3,7,101,18]
**Output:** 4

**Input:** nums = [0,1,0,3,2,3]
**Output:** 4

## Step-by-Step Approach

1. Use patience sorting with a tails array.
2. For each number, binary search its position in tails.
3. The length of tails is the answer.

## Time and Space Complexity

- **Time:** O(n log n)
- **Space:** O(n)
