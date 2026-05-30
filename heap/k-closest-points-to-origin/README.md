# K Closest Points to Origin

## Difficulty

Medium

## Problem Description

Given an array of points, return the k closest points to the origin.

## Constraints

- 1 <= k <= points.length <= 10^4
- -10^4 <= points[i][j] <= 10^4

## Example Input/Output

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

## Step-by-Step Explanation

1. Compute squared distance for each point.
2. Select the k smallest distances.

## Optimized Approach

Use a heap to get k smallest distances.

## Time Complexity

O(n log k)

## Space Complexity

O(k)
