# Two Sum

**Difficulty:** Easy

## Problem Description

Given an array of integers and a target value, return the indices of two distinct elements that add up to the target. You may assume exactly one valid answer exists, and you may not use the same element twice.

## Examples

**Input:** nums = [2, 7, 11, 15], target = 9
**Output:** [0, 1]

**Input:** nums = [3, 2, 4], target = 6
**Output:** [1, 2]

## Step-by-Step Approach

1. Iterate through the array while keeping a hash map of value -> index.
2. For each number, compute its complement (target - number).
3. If the complement is already in the map, return the stored index and the current index.
4. Otherwise, store the current number and index in the map.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
