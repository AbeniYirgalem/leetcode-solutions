# Contains Duplicate

**Difficulty:** Easy

## Problem Description

Given an integer array, return true if any value appears at least twice. Otherwise return false.

## Examples

**Input:** nums = [1,2,3,1]
**Output:** true

**Input:** nums = [1,2,3,4]
**Output:** false

## Step-by-Step Approach

1. Use a set to track seen numbers.
2. If a number is already in the set, a duplicate exists.
3. If the scan completes without duplicates, return false.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
