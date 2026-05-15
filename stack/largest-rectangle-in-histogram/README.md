# Largest Rectangle in Histogram

**Difficulty:** Hard

## Problem Description

Given an array of bar heights in a histogram, find the area of the largest rectangle.

## Examples

**Input:** heights = [2,1,5,6,2,3]
**Output:** 10

**Input:** heights = [2,4]
**Output:** 4

## Step-by-Step Approach

1. Use a stack of increasing bar indices.
2. When a shorter bar appears, pop from the stack and compute areas.
3. Use a sentinel height of 0 to flush remaining bars.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(n)
