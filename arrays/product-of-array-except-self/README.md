# Product of Array Except Self

**Difficulty:** Medium

## Problem Description

Given an integer array, return an array where each element is the product of all other elements. Do not use division and solve in O(n) time.

## Examples

**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

## Step-by-Step Approach

1. Build a prefix product array where prefix[i] is the product of nums[0..i-1].
2. Traverse from the end with a running suffix product and multiply into the prefix values.
3. The result uses O(1) extra space besides the output array.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1) extra space (excluding output)
