# Redundant Connection

## Difficulty

Medium

## Problem Description

Given an undirected graph that started as a tree with one extra edge added, return the edge that can be removed to restore a tree.

## Constraints

- 3 <= n <= 1000
- edges.length == n
- 1 <= u, v <= n

## Example Input/Output

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

## Step-by-Step Explanation

1. Use Union-Find to track connected components.
2. For each edge, if both nodes are already connected, it is redundant.

## Optimized Approach

Disjoint Set Union (Union-Find) with path compression and union by rank.

## Time Complexity

O(n alpha(n))

## Space Complexity

O(n)
