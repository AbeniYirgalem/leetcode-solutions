# Merge k Sorted Lists

**Difficulty:** Hard

## Problem Description

Given an array of sorted linked lists, merge them into a single sorted list and return its head.

## Examples

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]
**Output:** [1,1,2,3,4,4,5,6]

**Input:** lists = []
**Output:** []

## Step-by-Step Approach

1. Use a min-heap keyed by node value.
2. Push the head of each list into the heap.
3. Repeatedly pop the smallest node and push its next node.
4. Build the merged list as you pop.

## Time and Space Complexity

- **Time:** O(n log k)
- **Space:** O(k)
