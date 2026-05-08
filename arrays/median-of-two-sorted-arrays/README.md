# Median of Two Sorted Arrays

**Difficulty:** Hard

## Problem Description

Given two sorted arrays, return the median of the combined data set in O(log(m+n)) time.

## Examples

**Input:** nums1 = [1,3], nums2 = [2]
**Output:** 2.0

**Input:** nums1 = [1,2], nums2 = [3,4]
**Output:** 2.5

## Step-by-Step Approach

1. Use binary search on the smaller array to find a partition.
2. Ensure all elements on the left partitions are <= all elements on the right partitions.
3. Compute the median from the partition boundaries.

## Time and Space Complexity

- **Time:** O(log(min(m, n)))
- **Space:** O(1)
