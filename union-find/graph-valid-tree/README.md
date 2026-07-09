# Graph Valid Tree

## Difficulty

Medium

## Problem Description

Given n nodes and edges, determine if they form a valid tree (connected and acyclic).

## Constraints

- 1 <= n <= 2000
- 0 <= edges.length <= 5000

## Example Input/Output

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

## Step-by-Step Explanation

1. A tree must have exactly n-1 edges.
2. Use Union-Find to detect cycles.
3. If no cycles and edges count is n-1, it is a tree.

## Optimized Approach

Union-Find with early cycle detection.

## Time Complexity

O(n + e)

## Space Complexity

O(n)
