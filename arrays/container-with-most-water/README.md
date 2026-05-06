# Container With Most Water

**Difficulty:** Medium

## Problem Description

Given an array where each value represents a vertical line height, find the maximum area of water a container can store using two lines.

## Examples

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49

**Input:** height = [1,1]
**Output:** 1

## Step-by-Step Approach

1. Use two pointers at the ends of the array.
2. Compute the area using the shorter height.
3. Move the pointer pointing to the shorter height inward, because it limits the area.
4. Track the maximum area seen.

## Time and Space Complexity

- **Time:** O(n)
- **Space:** O(1)
