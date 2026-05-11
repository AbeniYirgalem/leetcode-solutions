# Trapping Rain Water

**Difficulty:** Hard

## Problem Description

Given an array of non-negative integers representing elevation heights, compute how much water it can trap after raining.

## Examples

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]
**Output:** 6

**Input:** height = [4,2,0,3,2,5]
**Output:** 9

## Step-by-Step Approach

1. Use two pointers at both ends.
2. Track the maximum height seen from the left and right.
3. Move the pointer with the smaller max height inward and accumulate trapped water.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
