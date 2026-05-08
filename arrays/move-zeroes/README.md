# Move Zeroes

**Difficulty:** Easy

## Problem Description

Given an array, move all zeros to the end while maintaining the relative order of non-zero elements. Do it in-place.

## Examples

**Input:** nums = [0,1,0,3,12]
**Output:** [1,3,12,0,0]

**Input:** nums = [0]
**Output:** [0]

## Step-by-Step Approach

1. Use a slow pointer to place the next non-zero element.
2. Iterate through the array and copy non-zero values forward.
3. Fill the remaining positions with zeros.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
