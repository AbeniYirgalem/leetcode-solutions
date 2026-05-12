# Clone Graph

**Difficulty:** Medium

## Problem Description

Given a reference to a node in a connected undirected graph, return a deep copy of the graph.

## Examples

**Input:** adjacency list = [[2,4],[1,3],[2,4],[1,3]]
**Output:** a deep copy of the same structure

**Input:** adjacency list = [[]]
**Output:** a single cloned node

## Step-by-Step Approach

1. Use BFS/DFS to traverse the graph.
2. Maintain a map from original node to cloned node.
3. For each edge, link the cloned neighbors accordingly.

## Time and Space Complexity

- **Time:** O(V + E)
- **Space:** O(V)
