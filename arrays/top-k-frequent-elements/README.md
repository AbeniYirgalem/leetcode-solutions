# Top K Frequent Elements

**Difficulty:** Medium

## Problem Description

Given an integer array, return the k most frequent elements.

## Examples

**Input:** nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

**Input:** nums = [1], k = 1
**Output:** [1]

## Step-by-Step Approach

1. Count frequencies with a hash map.
2. Use a min-heap of size k to keep the top k elements.
3. Extract the elements from the heap.

## Time and Space Complexity

- **Time:** O(n log k)
- **Space:** O(n)
