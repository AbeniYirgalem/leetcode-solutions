# Swim in Rising Water

## Difficulty

Hard

## Problem Description

Given a grid of elevations, you can move 4-directionally. Return the minimum time required to reach the bottom-right where time is the maximum elevation along the path.

## Constraints

- 1 <= n <= 50
- 0 <= grid[i][j] < n^2

## Example Input/Output

Input: grid = [[0,2],[1,3]]
Output: 3

## Step-by-Step Explanation

1. Use Dijkstra where path cost is the max elevation so far.
2. Always expand the lowest current cost.
3. The first time you reach the target is optimal.

## Optimized Approach

Min-heap with visited tracking.

## Time Complexity

O(n^2 log n)

## Space Complexity

O(n^2)
