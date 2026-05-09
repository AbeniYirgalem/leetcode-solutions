# Search in Rotated Sorted Array

**Difficulty:** Medium

## Problem Description

Given a rotated sorted array of unique integers and a target, return its index or -1 if it does not exist.

## Examples

**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4

**Input:** nums = [4,5,6,7,0,1,2], target = 3
**Output:** -1

## Step-by-Step Approach

1. Use binary search with a check for which side is sorted.
2. Decide whether the target lies in the sorted half or the other half.
3. Narrow the search interval until found or exhausted.

## Time and Space Complexity

- **Time:** O(log n)
- **Space:** O(1)
