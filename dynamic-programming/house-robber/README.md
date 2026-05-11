# House Robber

**Difficulty:** Medium

## Problem Description

You are given a list of non-negative integers representing money in houses along a street. Adjacent houses cannot both be robbed. Return the maximum amount you can rob.

## Examples

**Input:** nums = [1,2,3,1]
**Output:** 4

**Input:** nums = [2,7,9,3,1]
**Output:** 12

## Step-by-Step Approach

1. Use DP to track the best result up to each house.
2. At each house, choose between skipping or robbing it.
3. Keep only the last two states for O(1) space.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
