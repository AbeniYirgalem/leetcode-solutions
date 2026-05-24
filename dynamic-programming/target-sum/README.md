# Target Sum

## Difficulty

Medium

## Problem Description

Given an array of integers, assign '+' or '-' to each number so that the final sum equals target. Return the number of ways.

## Constraints

- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- -1000 <= target <= 1000

## Example Input/Output

Input: nums = [1,1,1,1,1], target = 3
Output: 5

## Step-by-Step Explanation

1. Use dynamic programming over indices.
2. Track how many ways to reach each sum so far.
3. Update counts for +num and -num.

## Optimized Approach

Use a hashmap to store counts of reachable sums.

## Time Complexity

O(n \* sum)

## Space Complexity

O(sum)
