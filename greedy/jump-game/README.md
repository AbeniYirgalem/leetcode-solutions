# Jump Game

## Difficulty

Medium

## Problem Description

Given an array where each element represents the maximum jump length, determine if you can reach the last index.

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

## Example Input/Output

Input: nums = [2,3,1,1,4]
Output: true

## Step-by-Step Explanation

1. Track the farthest index reachable so far.
2. If the current index is beyond this farthest reach, return false.
3. Update the farthest reach using nums[i].

## Optimized Approach

Greedy traversal with a single pass.

## Time Complexity

O(n)

## Space Complexity

O(1)
