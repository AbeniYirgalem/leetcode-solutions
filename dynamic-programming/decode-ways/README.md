# Decode Ways

**Difficulty:** Medium

## Problem Description

Given a string of digits, return the number of ways to decode it using the mapping A->1 ... Z->26.

## Examples

**Input:** s = "12"
**Output:** 2

**Input:** s = "226"
**Output:** 3

## Step-by-Step Approach

1. Use DP where dp[i] is the number of ways for prefix length i.
2. Add ways from single-digit decode and valid two-digit decode.
3. Keep only the last two states for O(1) space.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
