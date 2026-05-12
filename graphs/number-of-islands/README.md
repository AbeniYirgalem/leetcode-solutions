# Number of Islands

**Difficulty:** Medium

## Problem Description

Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is formed by horizontally or vertically adjacent lands.

## Examples

**Input:** grid = [["1","1","0","0"],["1","1","0","0"],["0","0","1","0"],["0","0","0","1"]]
**Output:** 3

**Input:** grid = [["0","0"],["0","0"]]
**Output:** 0

## Step-by-Step Approach

1. Scan each cell in the grid.
2. When land is found, start a DFS/BFS to mark all connected land as visited.
3. Each new unvisited land cell starts a new island count.

## Time and Space Complexity

- **Time:** O(rows \* cols)
- **Space:** O(rows \* cols) in worst-case recursion/stack
