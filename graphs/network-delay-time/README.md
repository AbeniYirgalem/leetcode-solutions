# Network Delay Time

## Difficulty

Medium

## Problem Description

Given times edges, number of nodes n, and a starting node k, find how long it takes for all nodes to receive a signal. Return -1 if not all nodes are reachable.

## Constraints

- 1 <= n <= 100
- 1 <= times.length <= 6000
- 1 <= k <= n
- 1 <= w <= 100

## Example Input/Output

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

## Step-by-Step Explanation

1. Build a directed graph with edge weights.
2. Use Dijkstra to compute shortest paths from k.
3. The answer is the maximum distance if all nodes are reachable.

## Optimized Approach

Dijkstra with a min-heap.

## Time Complexity

O(E log V)

## Space Complexity

O(E + V)
