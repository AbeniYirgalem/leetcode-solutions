# Longest Consecutive Sequence

**Difficulty:** Medium

## Problem Description

Given an unsorted array of integers, return the length of the longest consecutive elements sequence.

## Examples

**Input:** nums = [100,4,200,1,3,2]
**Output:** 4

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]
**Output:** 9

## Step-by-Step Approach

1. Insert all numbers into a set.
2. For each number, only start counting if it is the beginning of a sequence.
3. Expand forward while consecutive numbers exist.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
