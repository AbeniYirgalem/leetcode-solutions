# Burst Balloons

## Difficulty

Hard

## Problem Description

Given n balloons with numbers, burst them in an order to maximize coins. Bursting balloon i gives nums[left] _ nums[i] _ nums[right].

## Constraints

- 1 <= nums.length <= 300
- 0 <= nums[i] <= 100

## Example Input/Output

Input: nums = [3,1,5,8]
Output: 167

## Step-by-Step Explanation

1. Add virtual balloons with value 1 at both ends.
2. dp[l][r] is max coins from bursting balloons in (l, r).
3. Try every k as the last balloon to burst in (l, r).

## Optimized Approach

Interval DP with O(n^3) transitions.

## Time Complexity

O(n^3)

## Space Complexity

O(n^2)
