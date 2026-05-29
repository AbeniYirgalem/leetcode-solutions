# Jump Game II

## Difficulty

Medium

## Problem Description

Given an array where each element represents the maximum jump length, return the minimum number of jumps to reach the last index.

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

## Example Input/Output

Input: nums = [2,3,1,1,4]
Output: 2

## Step-by-Step Explanation

1. Track the farthest reach within the current jump range.
2. When you reach the end of the current range, increase jumps.
3. Update the range to the farthest reach.

## Optimized Approach

Greedy BFS-like layer expansion.

## Time Complexity

O(n)

## Space Complexity

O(1)
