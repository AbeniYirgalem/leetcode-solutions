# Find the Duplicate Number

## Difficulty

Medium

## Problem Description

Given an array of n + 1 integers where each integer is between 1 and n, find the duplicate number without modifying the array and using constant extra space.

## Constraints

- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n

## Example Input/Output

Input: nums = [1, 3, 4, 2, 2]
Output: 2

## Step-by-Step Explanation

1. Treat the array as a linked list where next = nums[i].
2. Use slow and fast pointers to find a cycle.
3. The entry to the cycle is the duplicate number.

## Optimized Approach

Floyd's cycle detection algorithm.

## Time Complexity

O(n)

## Space Complexity

O(1)
