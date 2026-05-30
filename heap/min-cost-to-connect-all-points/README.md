# Min Cost to Connect All Points

## Difficulty

Medium

## Problem Description

Given points in a plane, return the minimum cost to connect all points where cost is Manhattan distance.

## Constraints

- 1 <= points.length <= 1000
- -10^6 <= points[i][j] <= 10^6

## Example Input/Output

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

## Step-by-Step Explanation

1. Use Prim's algorithm to build a minimum spanning tree.
2. Track the minimum cost edge to each unvisited node.
3. Add the cheapest node each step.

## Optimized Approach

Prim's algorithm with O(n^2) distance updates.

## Time Complexity

O(n^2)

## Space Complexity

O(n)
