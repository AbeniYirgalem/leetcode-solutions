# Coin Change

**Difficulty:** Medium

## Problem Description

Given coin denominations and an amount, return the minimum number of coins needed to make up the amount. If it is not possible, return -1.

## Examples

**Input:** coins = [1,2,5], amount = 11
**Output:** 3

**Input:** coins = [2], amount = 3
**Output:** -1

## Step-by-Step Approach

1. Use bottom-up DP where dp[x] is the min coins for amount x.
2. Initialize dp[0] = 0 and others to infinity.
3. For each amount, try all coins and update dp.

## Time and Space Complexity

- **Time:** O(amount \* n)
- **Space:** O(amount)
